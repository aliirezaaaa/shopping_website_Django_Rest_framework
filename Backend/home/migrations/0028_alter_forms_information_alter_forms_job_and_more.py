# Generated by Django 4.0.3 on 2022-05-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_forms_mobile_alter_forms_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='information',
            field=models.TextField(default='N'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='job',
            field=models.CharField(default='N', max_length=100),
        ),
        migrations.AlterField(
            model_name='forms',
            name='landline',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='forms',
            name='length',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='forms',
            name='management',
            field=models.CharField(default='N', max_length=100),
        ),
        migrations.AlterField(
            model_name='forms',
            name='material',
            field=models.CharField(default='N', max_length=100),
        ),
        migrations.AlterField(
            model_name='forms',
            name='media_address',
            field=models.CharField(default='N', max_length=100),
        ),
        migrations.AlterField(
            model_name='forms',
            name='mobile',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='forms',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='forms',
            name='store_name',
            field=models.CharField(default='N', max_length=100),
        ),
        migrations.AlterField(
            model_name='forms',
            name='width',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
