# Generated by Django 3.1.4 on 2021-10-22 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20211022_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='reason',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requiremt',
            name='percentage',
            field=models.CharField(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], default='10', max_length=30),
        ),
    ]
