# Generated by Django 3.2.6 on 2021-08-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_alter_teacher_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(blank=True, max_length=230),
        ),
    ]