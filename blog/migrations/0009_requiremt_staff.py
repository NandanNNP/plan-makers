# Generated by Django 3.2.7 on 2021-10-16 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_requiremt'),
    ]

    operations = [
        migrations.AddField(
            model_name='requiremt',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.register'),
        ),
    ]
