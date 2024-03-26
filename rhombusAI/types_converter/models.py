from django.db import models
from django.conf import settings

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_size = models.IntegerField(default=0)
    schema = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"uploader: {self.uploader} -- file name: {self.file_name}"
    
    def save(self, *args, **kwargs):
        self.file_size = self.file.size  # Calculate the size in Bytes here
        super().save(*args, **kwargs)