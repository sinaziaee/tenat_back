from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from analyze import models
from scripts import extractor
import json
from analyze.api.serializer import *


def home_api(request):
    return HttpResponse('apis')


@api_view(['GET', ])
def temp(request):
    return Response('temp')


@api_view(['POST', ])
def upload(request):
    serializer = UploadSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        print('*'*100)
        obj = serializer.save()
        print(obj.file.path)
        extractor.apply(obj.file.path)
        return Response(serializer.data)
    return Response('failed')


class Upload(APIView):
    def post(self, args):
        # if self.request.FILES is not None:
        #     cur_file = self.request.FILES['file']
        # print(self.request.data)
        data = json.loads(json.dumps(self.request.data))
        print(data)
        print('------------------------------------------------------------------------------')
        # print(self.request.data)
        # print(self.request.body)
        # serializer = UploadSerializer(data=data)
        # if serializer.is_valid():
        #     return Response('status: unsuccessful', status=status.HTTP_201_CREATED)
        return Response('status: unsuccessful', status=status.HTTP_400_BAD_REQUEST)

    def get(self, args):
        print('here')
        return Response('status: successful', status=status.HTTP_200_OK)

    def update(self, args):
        pass

    def delete(self, args):
        pass
