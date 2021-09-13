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
    documents = CompressFile.objects.all()
    if True:
        FileField(label='Select a file', help_text='max. 10 megabytes')
        # Handle file upload
        if request.method == 'POST':
            if request.POST.get('delete_items') is not None:
                id = request.POST.get('delete_items')
                id = str(id).replace('delete ', '')
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
                    founded_file.delete()
                    deleter(founded_file.name)
                newdoc = CompressFile(file=cur_file, name=cur_name)
                newdoc.save()
                start_automated_scripts(newdoc)
                # Redirect to the zip_upload.html page
                return render(request, 'compress/upload.html',
                              {'status': 'File uploaded successfully', 'form': ZipFileForm(), 'files': documents})
        else:
            print('get')
            print(documents)

        # Render list page with the documents and the form
        return render(request, 'compress/upload.html', {'form': ZipFileForm(), 'files': documents})
    else:
        return redirect('loginuser')


def deleter(filename):
    new_filename = str(filename).replace('.rar', '').replace('.zip', '')
    dirname = os.path.dirname(__file__)
    path = pathlib.Path(dirname).parent
    data_path = os.path.join(path, f'media/data/{new_filename}')
    result_path = os.path.join(path, f'media/result/{new_filename}')
    doc_zip_path = os.path.join(path, f'media/docs/zips/{filename}')
    shutil.rmtree(data_path)
    shutil.rmtree(result_path)
    os.remove(doc_zip_path)


def start_automated_scripts(newdoc):
    extractor.apply(newdoc.file.path)
