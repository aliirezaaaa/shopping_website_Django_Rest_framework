# Generated by Django 4.0.3 on 2022-05-07 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_offsetform_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Offset', 'Offset'), ('Sublimition', 'Sublimition')], max_length=30)),
                ('store_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('management', models.CharField(max_length=100)),
                ('media_address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('landline', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('material', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='order')),
                ('length', models.PositiveIntegerField(default=10)),
                ('width', models.PositiveIntegerField(default=10)),
            ],
        ),
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
        migrations.AddField(
            model_name='product',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.forms'),
        ),
    ]
