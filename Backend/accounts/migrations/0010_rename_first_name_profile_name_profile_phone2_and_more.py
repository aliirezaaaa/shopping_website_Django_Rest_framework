# Generated by Django 4.0.3 on 2022-04-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='province',
            field=models.CharField(max_length=50, null=True),
        ),
    ]