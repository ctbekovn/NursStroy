# Generated by Django 3.2.7 on 2022-02-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_auto_20220213_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='objects',
            name='floors',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
