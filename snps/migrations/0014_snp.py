# Generated by Django 2.0.5 on 2018-05-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0013_tost'),
    ]

    operations = [
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chrom', models.IntegerField()),
                ('Chrom_pos', models.IntegerField()),
                ('Rsid', models.IntegerField()),
            ],
        ),
    ]
