# Generated by Django 2.0.5 on 2018-05-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0019_snp2phenotype2ref_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='snp2phenotype2ref',
            name='pvalue',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]