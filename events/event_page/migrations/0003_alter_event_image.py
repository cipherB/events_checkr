# Generated by Django 3.2.6 on 2021-08-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_page', '0002_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(height_field=2000, upload_to='', width_field=1920),
        ),
    ]
