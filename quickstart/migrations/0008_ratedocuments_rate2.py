# Generated by Django 4.0 on 2021-12-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_alter_documents_rate_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratedocuments',
            name='rate2',
            field=models.IntegerField(default=1, verbose_name='hksdhsd'),
            preserve_default=False,
        ),
    ]