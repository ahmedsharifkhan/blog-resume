# Generated by Django 3.2.8 on 2021-11-01 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_auto_20211101_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincontent',
            old_name='main_content',
            new_name='maincontent',
        ),
        migrations.RenameField(
            model_name='maincontent',
            old_name='main_title',
            new_name='maintitle',
        ),
    ]
