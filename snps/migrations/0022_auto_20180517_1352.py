# Generated by Django 2.0.5 on 2018-05-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0021_auto_20180517_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='Journal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='reference',
            name='Title',
            field=models.CharField(max_length=200),
        ),
    ]
