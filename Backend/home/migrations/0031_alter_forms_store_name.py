# Generated by Django 4.0.3 on 2022-05-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_forms_information_alter_forms_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='store_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]