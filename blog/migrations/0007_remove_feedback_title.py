# Generated by Django 3.2.7 on 2021-10-09 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_complaints_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='title',
        ),
    ]