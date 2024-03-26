from django.contrib import admin
from .models import UploadedFile

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'file_name', 'schema', 'file_size', 'uploaded_at',  'uploader')

admin.site.register(UploadedFile, UploadedFileAdmin)