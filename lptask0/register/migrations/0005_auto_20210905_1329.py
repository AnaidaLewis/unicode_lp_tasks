# Generated by Django 3.2.6 on 2021-09-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20210905_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='https://icon-library.com/images/no-profile-picture-icon/no-profile-picture-icon-14.jpg', null=True, upload_to=''),
        ),
    ]
