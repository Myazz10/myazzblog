# Generated by Django 3.0.8 on 2020-07-30 01:45

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200729_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='soft_tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('random', 'Random'), ('nice', 'Nice')], max_length=11, null=True),
        ),
    ]
