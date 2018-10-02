# Generated by Django 2.1.1 on 2018-10-01 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20181002_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('PERSONAL', 'PERSONAL'), ('WORK', 'WORK')], default='PERSONAL', max_length=10),
        ),
    ]
