# Generated by Django 4.0.3 on 2022-05-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_forms_information_alter_forms_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='landline',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='forms',
            name='length',
            field=models.PositiveIntegerField(blank=True, default=10),
        ),
        migrations.AlterField(
            model_name='forms',
            name='mobile',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='forms',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='forms',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=10),
        ),
    ]
