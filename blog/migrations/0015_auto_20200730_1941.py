# Generated by Django 3.0.8 on 2020-07-31 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_soft_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category_tags',
            field=models.CharField(choices=[('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Technology', 'Technology'), ('Food', 'Food'), ('Photography', 'Photography')], max_length=20, null=True),
        ),
    ]
