# Generated by Django 2.0.5 on 2018-08-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180717_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(upload_to='video'),
        ),
    ]
