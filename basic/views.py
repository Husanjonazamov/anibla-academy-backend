import os

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from basic import serializers
from basic.models import ClickOrder
from pyclick import PyClick
from pyclick.views import PyClickMerchantAPIView
from django.utils import timezone

from botusers.models import BotUser
from helpers.send_message_user import send_message


class CreateClickOrderView(CreateAPIView):
    serializer_class = serializers.ClickOrderSerializer

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        user = request.data.get('user')
        user = BotUser.objects.get(user_id=user)

        order = ClickOrder.objects.create(
            amount=amount,
            user=user
        )

        return_url = 'https://t.me/anibl_academ_uz_bot?start=lessons'
        url = PyClick.generate_url(
            order_id=order.id, amount=str(amount), return_url=return_url)

        return Response({"url": url})


class OrderCheckAndPayment(PyClick):
    def check_order(self, order_id: str, amount: str):
        if order_id:
            try:
                order = ClickOrder.objects.get(id=order_id)
                if int(amount) == order.amount:
                    return self.ORDER_FOUND
                else:
                    return self.INVALID_AMOUNT
            except ClickOrder.DoesNotExist:
                return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        """ Эта функция вызывается после успешной оплаты """
        try:
            order = ClickOrder.objects.get(id=order_id)
            order.is_paid = True
            order.save()

            user = BotUser.objects.get(user_id=order.user.user_id)
            user.is_purchased = True
            user.purchase_time = timezone.now()
            user.save()

            send_message(
                message=os.environ.get('SUCCESS_PAYMENT_MESSAGE'),
                chat_id=order.user.user_id
            )

        except ClickOrder.DoesNotExist:
            print(f"no order object not found: {order_id}")


class OrderTestView(PyClickMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment
