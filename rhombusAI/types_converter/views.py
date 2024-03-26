from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# from rest_framework import permissions

from .src.data_type_converter import DataTypeConverter
from . import forms
from . import models
from . import serializers


@login_required
def home(request:HttpRequest):
    files = models.UploadedFile.objects.all()
    return render(request, 'types_converter/home.html', {'files': files})

@login_required
def file_upload(request:HttpRequest):
    if request.method == 'POST':
        form = forms.FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.uploader = request.user
            file.save()
            return redirect('home')
    else:
        form = forms.FileForm()
    return render(request, 'types_converter/file_upload.html', {'form': form})

class UploadedFileViewSet(ModelViewSet):
    serializer_class = serializers.FileUploadSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Add this line

    def get_queryset(self):
        return models.UploadedFile.objects.all().order_by('-uploaded_at')
    
    def create(self, request:HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save(uploader=self.request.user) 
        converter = DataTypeConverter(instance.file.path)
        converter.load_data(nrows=1000)
        instance.schema = converter.infer_schema()
        instance.save()
        
    @action(detail=True, methods=['get'])
    def schema(self, request, pk=None):
        file = self.get_object()
        if file.schema is None:
            converter = DataTypeConverter(file.file.path)
            converter.load_data(nrows=1000)
            file.schema = converter.infer_schema()
            file.save()
            
        return Response({"schema": file.schema}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def sample(self, request, pk=None):
        file = self.get_object()
        n_rows = int(request.GET.get('rows', 10))
        converted = request.GET.get('converted', 'false')

        converter = DataTypeConverter(file_path=file.file.path, schema=file.schema)
        converter.load_data(nrows=n_rows)
        if converted == 'true':
            converter.convert()
        extracted_data = converter.df.to_dict()

        return Response({"data": extracted_data}, status=status.HTTP_200_OK)