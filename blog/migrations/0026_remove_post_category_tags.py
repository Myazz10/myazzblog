# Generated by Django 3.0.8 on 2020-08-06 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_tags',
        ),
    ]
