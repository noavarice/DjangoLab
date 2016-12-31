from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FileHandlerForm
from .models import FileHandler
from django.conf import settings
import string, random
from base62 import encode, decode

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
    url = obj.file_to_store.name.split('/')
    return render(request, 'FileHandler/download.html', { 'url': unique_file_url, 'path': url[len(url) - 1]})

def temporary_download_page(request):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=%s' % MEDIA_ROOT + request.path
    return response    
