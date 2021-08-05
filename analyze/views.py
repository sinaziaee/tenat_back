from django.shortcuts import render, HttpResponse, redirect
import pathlib
import shutil
from .forms import ZipFileForm
from .models import CompressFile
from django.forms import FileField
import os
from scripts import extractor


def home(request):
    return HttpResponse('home')


def compress_view(request):
    documents = CompressFile.objects.filter(uploader=request.user)

    if request.user.is_superuser:
        FileField(label='Select a file', help_text='max. 10 megabytes')
        # Handle file upload
        print('-' * 100)
        if request.method == 'POST':
            if request.POST.get('delete_items') is not None:
                id = request.POST.get('delete_items')
                id = str(id).replace('delete ', '')
                print(id)
                file = CompressFile.objects.get(file_id=id)
                file.delete()
                deleter(file.name)
                documents = CompressFile.objects.filter(uploader=request.user)
                return render(request, 'compress/upload.html',
                              {'status': 'File deleted successfully', 'form': ZipFileForm(), 'files': documents})
            else:
                cur_user = request.user
                cur_file = request.FILES['docfile']
                cur_name = str(cur_file)
                founded_file = CompressFile.objects.filter(name=cur_name)
                if len(founded_file) != 0:
                    founded_file = CompressFile.objects.get(name=cur_name)
                    print('founded: ', founded_file.name)
                    founded_file.delete()
                    deleter(founded_file.name)
                # form = ZipFileForm()
                # if form.is_valid():
                newdoc = CompressFile(file=cur_file, name=cur_name, uploader=cur_user)
                newdoc.save()
                start_automated_scripts(newdoc)
                # Redirect to the zip_upload.html page
                return render(request, 'compress/upload.html',
                              {'status': 'File uploaded successfully', 'form': ZipFileForm(), 'files': documents})
        else:
            print(documents)

        # Render list page with the documents and the form
        return render(request, 'compress/upload.html', {'form': ZipFileForm(), 'files': documents})
    else:
        return redirect('loginuser')


def deleter(filename):
    new_filename = str(filename).replace('.rar', '').replace('.zip', '')
    dirname = os.path.dirname(__file__)
    path = pathlib.Path(dirname).parent
    print('*' * 100)
    data_path = os.path.join(path, f'media_cdn/data/{new_filename}')
    result_path = os.path.join(path, f'media_cdn/result/{new_filename}')
    doc_zip_path = os.path.join(path, f'media_cdn/docs/zips/{filename}')
    print('*' * 100)
    shutil.rmtree(data_path)
    shutil.rmtree(result_path)
    os.remove(doc_zip_path)


def start_automated_scripts(newdoc):
    print(newdoc.file.path)
    extractor.apply(newdoc.file.path)
