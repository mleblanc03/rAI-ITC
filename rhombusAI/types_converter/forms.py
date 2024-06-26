from django import forms
from . import models

class FileForm(forms.ModelForm):
    class Meta:
        model = models.UploadedFile
        fields = ['file', 'file_name']