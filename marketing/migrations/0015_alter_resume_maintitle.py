# Generated by Django 3.2.8 on 2021-12-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0014_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='maintitle',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
