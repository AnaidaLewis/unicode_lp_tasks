# Generated by Django 3.2.6 on 2021-09-03 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task0', '0002_todolist_due_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='due_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]