# Generated by Django 3.1 on 2023-05-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0005_merge_20230514_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
