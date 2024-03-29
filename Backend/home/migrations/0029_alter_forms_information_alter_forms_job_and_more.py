# Generated by Django 4.0.3 on 2022-05-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_forms_information_alter_forms_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='landline',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='length',
            field=models.PositiveIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='management',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='media_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='mobile',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='store_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=10, null=True),
        ),
    ]
