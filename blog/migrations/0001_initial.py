# Generated by Django 3.2.8 on 2021-10-09 14:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.CharField(max_length=20)),
                ('author_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
