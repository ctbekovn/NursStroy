# Generated by Django 3.2.7 on 2022-02-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_objects_floors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectsimages',
            options={},
        ),
        migrations.AddField(
            model_name='objects',
            name='status',
            field=models.CharField(choices=[('Строится', 'Строится'), ('Сдан в эксплуатацию', 'Сдан в эксплуатацию')], default='Строится', max_length=255),
        ),
    ]