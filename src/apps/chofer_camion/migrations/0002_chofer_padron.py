# Generated by Django 4.0.5 on 2022-07-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padron', '0001_initial'),
        ('chofer_camion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chofer',
            name='padron',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='padron.padron'),
        ),
    ]
