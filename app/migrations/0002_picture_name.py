# Generated by Django 4.2.2 on 2023-09-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
