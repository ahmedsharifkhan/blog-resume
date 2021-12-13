# Generated by Django 3.2.8 on 2021-11-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0012_aboutbulletin'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socilaTitle', models.CharField(blank=True, max_length=100, null=True)),
                ('socilaLink', models.CharField(blank=True, max_length=100, null=True)),
                ('socilColor', models.CharField(blank=True, max_length=100, null=True)),
                ('featured', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
