# Generated by Django 4.0.3 on 2022-05-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_forms_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='store_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
