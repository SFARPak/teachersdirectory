# Generated by Django 3.2.6 on 2021-08-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_remove_teacher_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(blank=True, max_length=230, unique=True),
        ),
    ]
