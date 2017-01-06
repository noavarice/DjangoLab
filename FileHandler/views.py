from django.shortcuts   import render, get_object_or_404
from django.http        import HttpResponseRedirect, HttpResponse
from forms              import FileHandlerForm
from models             import FileHandler
from base62             import encode, decode
import Lab5.settings
import string, random

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
    return render(request, 'FileHandler/successfully_uploaded.html', { 'address': request.path.split('/')[-1]})

def download(request):
    unique_file_url = request.path.split('/')[-1]
    obj = get_object_or_404(FileHandler, pk = decode(unique_file_url))
    filename = obj.file_to_store.name.split('/')[-1]
    return render(request, 'FileHandler/download_layout.html', { 'url': unique_file_url, 'path': filename})

def temporary_download_page(request):
    response = HttpResponse()
    full_filename = os.path.join(MEDIA_ROOT, request.path.split('/')[-1])
    response['Content-Type'] = from_file((full_filename, filename), mime = True)
    response['Content-Disposition'] = "attachment; filename='%s'" % full_filename
    return response    
