# Generated by Django 2.0.5 on 2018-05-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0012_auto_20180515_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(default='', max_length=100)),
                ('f2', models.CharField(default='', max_length=200)),
            ],
        ),
    ]