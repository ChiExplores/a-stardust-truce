# Generated by Django 2.2.3 on 2019-09-14 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20190913_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_structure',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='data_structure',
            name='methods',
            field=models.ManyToManyField(blank=True, to='main_app.Method'),
        ),
        migrations.AlterField(
            model_name='data_structure',
            name='properties',
            field=models.ManyToManyField(blank=True, to='main_app.Property'),
        ),
    ]
