# Generated by Django 3.2.8 on 2021-11-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0010_aboutsocial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsocial',
            name='socilColor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
