# Generated by Django 2.1.3 on 2020-02-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200213_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile_num',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]