# Generated by Django 2.1.3 on 2020-02-16 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200216_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='disability_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.DisabilityCard'),
        ),
    ]
