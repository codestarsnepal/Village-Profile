# Generated by Django 2.1.3 on 2020-02-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200220_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='foreign_stay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='has_chronic_disease',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_child_marriage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_vaccinated',
            field=models.IntegerField(default=0),
        ),
    ]
