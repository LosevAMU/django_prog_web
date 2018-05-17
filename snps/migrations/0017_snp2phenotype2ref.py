# Generated by Django 2.0.5 on 2018-05-17 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0016_disease_trait'),
    ]

    operations = [
        migrations.CreateModel(
            name='SNP2Phenotype2Ref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Snp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snps.SNP')),
            ],
        ),
    ]