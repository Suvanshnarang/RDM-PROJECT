# Generated by Django 4.0.4 on 2022-07-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
