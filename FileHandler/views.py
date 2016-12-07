from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FileHandlerForm

# Create your views here.

def handle(request):
    if request.method == 'POST':
        form = FileHandlerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/load/success')
    else:
        form = FileHandlerForm()
    return render(request, 'FileHandler/index.html', { 'form': form })

def succeed(request):
    return HttpResponse('File was successfully uploaded')
