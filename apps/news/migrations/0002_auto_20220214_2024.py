# Generated by Django 3.2.7 on 2022-02-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='detail',
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
