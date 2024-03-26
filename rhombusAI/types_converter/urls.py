from django.urls import path
import types_converter.views as views

urlpatterns = [
    path("",views.home, name='home'),
    path("upload/", views.file_upload, name="file_upload"),
]
