# Generated by Django 2.2.5 on 2019-09-13 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_element_dimension'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_structure',
            name='element',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Element'),
            preserve_default=False,
        ),
    ]
