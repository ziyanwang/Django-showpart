# Generated by Django 2.0.5 on 2018-07-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180607_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='Media/img')),
                ('video', models.FileField(upload_to='Media/video')),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
