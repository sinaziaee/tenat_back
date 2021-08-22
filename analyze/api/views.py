from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from scripts import extractor, list_files_and_sizes, tokenizer
from scripts.normalize import english_normalizer, persian_normalizer
from scripts.stem import english_stemmer, persian_stemmer
from scripts.stop_word_removal import english_stop_word_removal, persian_stop_word_removal
from analyze.api.serializer import *
import time


def home_api(request):
    return HttpResponse('apis')


@api_view(['GET', ])
def temp(request):
    return Response('temp')


@api_view(['POST', 'GET'])
def upload(request):
    print('*' * 100)
    if request.method == 'POST':
        print('yess')
        print(str(request.data))

        serializer = UploadSerializer(data=request.data)
        print('='*100)
        if serializer.is_valid():
            print('-' * 100)
            val_data = serializer.validated_data
            file_name = val_data['file']
            temp = models.CompressFile.objects.filter(file=file_name)
            rand_int = round(time.time() * 1000)
            print(temp)
            print('*' * 100)
            print(file_name)
            print(models.CompressFile.objects.filter(file=file_name).exists())
            if models.CompressFile.objects.filter(name=val_data['name']).exists():
                folder_name = val_data['name'] + '_' + str(rand_int)
                print(folder_name)
                obj = models.CompressFile(name=val_data['name'], file=val_data['file'])
                obj.file.name = folder_name
                obj.save()
            else:
                obj = models.CompressFile(name=val_data['name'], file=val_data['file'])
                obj.file.name = val_data['name']
                obj.save()
                print(obj.file.path)
            map_list = extractor.apply(obj.file.path)
            return Response(map_list, status=status.HTTP_200_OK)
        return Response('failed')
    elif request.method == 'GET':
        print('-' * 100)
        name = request.GET.get('name')  
        id = request.GET.get('id')
        if id is not None:
            file = models.CompressFile.objects.get(file_id=id)
        elif name is not None:
            file = models.CompressFile.objects.get(name=id)
        else:
            file = models.CompressFile.objects.get(file=request.GET.get('file'))
        folder_name = file.file.path
        folder_path = f'media/data/{folder_name}/'
        map_list = list_files_and_sizes.apply(folder_path)
        print(map_list)
        return Response(map_list)
    else:
        pass


@api_view(['POST'])
def tokenize(request):
    print('*'*100)
    new_map = request.POST
    name = new_map.get('name')
    from_path = new_map.get('from')
    language = new_map.get('language')
    algorithm = new_map.get('algorithm')
    splitter = new_map.get('splitter')
    print(name)
    print(from_path)
    print(splitter)
    try:
        files_list = tokenizer.apply(name=name, splitter=splitter,
                                     from_path=from_path, to_path='tokenized')
        return Response(files_list, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('failed', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def normalize(request):
    new_map = request.POST
    name = new_map.get('name')
    from_path = new_map.get('from')
    language = new_map.get('language')
    try:
        if language == 'persian':
            result = persian_normalizer.apply(name=name, from_path=from_path, to_path='normalized')
        else:
            result = english_normalizer.apply(name=name, from_path=from_path, to_path='normalized')
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('failed', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def stem(request):
    new_map = request.POST
    name = new_map.get('name')
    from_path = new_map.get('from')
    language = new_map.get('language')
    algorithm = new_map.get('algorithm')
    if language == 'Persian':
        result = persian_stemmer.apply(from_path=from_path, algorithm=algorithm, to_path='stemmed', name=name)
    elif language == 'English':
        result = english_stemmer.apply(from_path=from_path, algorithm=algorithm, to_path='stemmed', name=name)
    else:
        result = english_stemmer.apply(from_path=from_path, algorithm=algorithm, to_path='stemmed', name=name)
    if result is not None and len(result) != 0:
        return Response(result, status=status.HTTP_200_OK)
    return Response('failed', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def remove_stop_word(request):
    new_map = request.POST
    name = new_map.get('name')
    from_path = new_map.get('from')
    language = new_map.get('language')
    if language == 'Persian':
        result = persian_stop_word_removal.apply(from_path=from_path, to_path='stop_word', name=name)
    elif language == 'English':
        result = english_stop_word_removal.apply(from_path=from_path, to_path='stop_word', name=name)
    else:
        result = english_stop_word_removal.apply(from_path=from_path, to_path='stop_word', name=name)
    if result is not None and len(result) != 0:
        return Response(result, status=status.HTTP_200_OK)
    return Response('failed', status=status.HTTP_400_BAD_REQUEST)
