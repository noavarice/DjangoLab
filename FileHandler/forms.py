from django.forms import ModelForm
from FileHandler.models import FileHandler

class FileHandlerForm(ModelForm):
    class Meta:
        model = FileHandler
        exclude = ['date']
