from django.shortcuts   import render, get_object_or_404
from django.http        import HttpResponseRedirect, HttpResponse, FileResponse
from forms              import FileHandlerForm
from models             import FileHandler, Advertisement
from base62             import encode, decode
from magic              import from_file
from Lab5.settings      import MEDIA_ROOT
from random             import randint
from django.utils       import timezone
from dateutil.parser    import parse
from django.utils.encoding import smart_str
import os
import urllib
import string, random

def upload(request):
    if request.method == 'POST':
        form = FileHandlerForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit = False)
            temp.bound_advert = Advertisement.objects.get(id = randint(1, Advertisement.objects.latest('id').id))
            temp.save()
            return HttpResponseRedirect('/uploaded/%s' % encode(temp.id))
    else:
        form = FileHandlerForm()
    return render(request, 'FileHandler/index.html', { 'form': form })

def succeed(request):
    return render(request, 'FileHandler/successfully_uploaded.html', { 'address': request.path.split('/')[-1]})

def download(request):
    unique_file_url = request.path.split('/')[-1]
    obj = get_object_or_404(FileHandler, pk = decode(unique_file_url))
    if not request.session.session_key:
        request.session.save()
    request.session['opening_time'] = str(timezone.now())
    return render(request, 'FileHandler/download_layout.html', {
        'url': unique_file_url,
        'file_name': obj.file_to_store.name.split('/')[-1],
        'advert': obj.bound_advert.content_file,
        'time': obj.bound_advert.exposition_time * 1000 })

def temporary_download_page(request):
    url = request.path.split('/')[-1]
    obj = get_object_or_404(FileHandler, pk = decode(url))
    path = obj.file_to_store.name
    if os.path.exists(path):
        exposition_time = obj.bound_advert.exposition_time
        rs = request.session
        key_name = 'opening_time'
        if not rs.session_key or key_name not in rs or (timezone.now() - parse(rs[key_name])).total_seconds() < exposition_time:
            return HttpResponseRedirect('/download/%s' % request.path.split('/')[-1])
        del request.session[key_name]
        response = FileResponse(open(path, 'rb'), content_type = 'application/force-download')
        response['Content-Disposition'] = 'inline; filename="%s"' % os.path.basename(path)
        return response    
    return HttpResponseNotFound()
