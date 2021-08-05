from django.db import models
from django.contrib.auth.models import User


class CompressFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(null=False, blank=False, upload_to='docs/zips/')
    name = models.CharField(null=True, blank=True, max_length=100)
    uploader = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.file_id} Name: {self.name}, Path: {str(self.file.path).split("/")[-1]}'

