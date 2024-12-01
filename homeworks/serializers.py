from rest_framework import serializers
from env import BOT_TOKEN
from .models import Homework, HomeWorkFiles
import requests


class HomeWorkFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWorkFiles
        fields = ('file_id', 'file_type')


class HomeworksSeralizers(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField()), write_only=True
    )
    file_details = HomeWorkFilesSerializer(many=True, read_only=True)

    class Meta:
        model = Homework
        fields = ('lesson', 'user', 'is_successful', 'files', 'file_details')
        extra_kwargs = {
            'is_successful': {'default': 'tekshirilmoqda'}
        }

    def create(self, validated_data):
        # Extract files from the incoming data
        files_data = validated_data.pop('files', [])
        homework = Homework.objects.create(**validated_data)

        # Process files
        for file_data in files_data:
            file_id = file_data['file_id']
            file_type = file_data['type']

            # Get the file URL from Telegram API
            file_info = requests.get(
                f'https://api.telegram.org/bot{
                    BOT_TOKEN}/getFile?file_id={file_id}'
            ).json()
            file_url = f'https://api.telegram.org/file/bot{
                BOT_TOKEN}/{file_info["result"]["file_path"]}'

            # Create HomeWorkFiles entry
            HomeWorkFiles.objects.create(
                homework=homework,
                file_id=file_url,
                file_type=file_type
            )

        return homework
