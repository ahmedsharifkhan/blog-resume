# Generated by Django 3.2.8 on 2021-11-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_auto_20211101_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincontent',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
