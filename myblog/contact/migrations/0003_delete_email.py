# Generated by Django 3.0 on 2019-12-14 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='email',
        ),
    ]
