# Generated by Django 5.0.3 on 2024-03-22 00:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("types_converter", "0002_uploadedfile_file_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadedfile",
            name="schema",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
