# data_processor/serializers.py
from rest_framework import serializers
from types_converter.models import UploadedFile

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['pk','file', 'file_name', 'file_size', 'schema', 'uploaded_at', 'uploader']
        read_only_fields = ['file_size', 'schema', 'uploaded_at', 'uploader'] 
    
    def validate_file_name(self, value):
        if UploadedFile.objects.filter(file_name=value).exists():
            raise serializers.ValidationError("File already exists")
        if value is None:
            raise serializers.ValidationError("File name cannot be empty")
        return value
