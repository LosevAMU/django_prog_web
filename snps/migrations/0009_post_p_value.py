# Generated by Django 2.0.5 on 2018-05-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0008_auto_20180515_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='P_VALUE',
            field=models.FloatField(default=0),
        ),
    ]
