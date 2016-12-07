from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FileHandlerForm
from .models import FileHandler
import string, random

# Create your views here.

def upload(request):
    if request.method == 'POST':
        form = FileHandlerForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit = False)
            chars = string.ascii_letters + string.digits
            temp.unique_url = ''.join(random.choice(chars) for _ in range(8))
            temp.save()
            return HttpResponseRedirect('/uploaded/%s' % temp.unique_url)
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
    obj = get_object_or_404(FileHandler, pk = unique_file_url)
    return render(request, 'FileHandler/download.html', { 'obj': obj })
