# Generated by Django 4.2.2 on 2023-09-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_picture_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
