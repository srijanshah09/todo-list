# Generated by Django 2.1.1 on 2018-10-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20181002_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_priority',
            field=models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='LOW', max_length=10),
        ),
    ]