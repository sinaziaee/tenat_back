from rest_framework import serializers
from analyze import models


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompressFile
        # fields = ['file', 'name']
        fields = '__all__'
