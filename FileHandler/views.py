from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileHandlerForm

# Create your views here.

def handle(request):
    if request.method == 'POST':
        form = FileHandlerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = FileHandlerForm()
    return render(request, 'FileHandler/index.html', { 'form': form })
