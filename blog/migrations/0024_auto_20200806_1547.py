# Generated by Django 3.0.8 on 2020-08-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200806_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_tags',
            field=models.CharField(choices=[('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Technology', 'Technology'), ('Food', 'Food'), ('Photography', 'Photography')], max_length=20, null=True),
        ),
    ]