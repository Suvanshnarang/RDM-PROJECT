# Generated by Django 4.0.4 on 2022-06-02 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='product_name',
        ),
    ]
