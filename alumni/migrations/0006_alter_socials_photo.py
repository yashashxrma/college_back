# Generated by Django 3.2.5 on 2021-08-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_socials_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socials',
            name='photo',
            field=models.FileField(null=True, upload_to='media\\pics'),
        ),
    ]