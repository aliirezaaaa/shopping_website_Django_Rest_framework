# Generated by Django 4.0.3 on 2022-05-01 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_offsetform_product_offsetform_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OffsetForm',
            new_name='Form',
        ),
    ]
