from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FileHandlerForm
from .models import FileHandler
import Lab5.settings
import string, random
from base62 import encode, decode
from magic import from_file
import os

def upload(request):
    if request.method == 'POST':
        form = FileHandlerForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save()
            return HttpResponseRedirect('/uploaded/%s' % encode(temp.id))
    else:
        form = FileHandlerForm()
    return render(request, 'FileHandler/index.html', { 'form': form })

def succeed(request):
    url = request.path.split('/')
    unique_file_url = url[len(url) - 1]
    return render(request, 'FileHandler/successfully_uploaded.html', { 'address': unique_file_url })

def download(request):
    url = request.path.split('/')
    unique_file_url = url[len(url) - 1]
    obj = get_object_or_404(FileHandler, pk = decode(unique_file_url))
    return render(request, 'FileHandler/download.html', { 'url': unique_file_url, 'path': obj.file_to_store.name.split('/')[-1]})

def temporary_download_page(request):
    response = HttpResponse()
<<<<<<< HEAD
    full_filename = os.path.join(MEDIA_ROOT, request.path.split('/')[-1])
    response['Content-Type'] = from_file(full_filename, filename), mime = True)
    response['Content-Disposition'] = "attachment; filename='%s'" % full_filename
=======
    response['Content-Disposition'] = "attachment; filename='%s'" % MEDIA_ROOT + request.path
>>>>>>> dd62bb8535351f8c318bbac60de993ae6e2cc340
    return response    
