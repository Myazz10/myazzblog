# Generated by Django 3.0.8 on 2020-08-12 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200809_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='popular_posts', to='blog.Post')),
            ],
        ),
    ]
