# Generated by Django 2.0.4 on 2018-05-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe',
            name='events',
            field=models.ManyToManyField(blank=True, to='tribes.Event'),
        ),
    ]