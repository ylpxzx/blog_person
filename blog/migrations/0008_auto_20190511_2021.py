# Generated by Django 2.0 on 2019-05-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190511_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image1',
        ),
    ]
