# Generated by Django 2.0.5 on 2018-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snps', '0003_post_pubmedid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
