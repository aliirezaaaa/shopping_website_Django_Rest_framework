# Generated by Django 4.0.3 on 2022-05-07 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_offsetform_sublimitionform_remove_product_form_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sublimitionform',
            name='category',
        ),
        migrations.DeleteModel(
            name='OffsetForm',
        ),
        migrations.DeleteModel(
            name='SublimitionForm',
        ),
    ]