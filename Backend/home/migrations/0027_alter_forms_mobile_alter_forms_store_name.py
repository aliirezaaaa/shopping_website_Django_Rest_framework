# Generated by Django 4.0.3 on 2022-05-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_forms_landline_alter_forms_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='store_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
