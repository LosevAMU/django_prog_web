# Generated by Django 2.0.5 on 2018-05-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0015_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease_trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
    ]
