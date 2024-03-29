# Generated by Django 4.0.3 on 2022-05-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_forms_landline_alter_forms_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='landline',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
