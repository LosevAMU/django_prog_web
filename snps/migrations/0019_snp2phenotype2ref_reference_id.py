# Generated by Django 2.0.5 on 2018-05-17 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0018_snp2phenotype2ref_disease_trait_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='snp2phenotype2ref',
            name='Reference_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snps.Reference'),
            preserve_default=False,
        ),
    ]
