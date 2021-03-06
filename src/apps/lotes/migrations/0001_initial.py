# Generated by Django 4.0.5 on 2022-07-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('padron', '0001_initial'),
        ('establecimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lotes',
            fields=[
                ('numero_lote', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.establecimiento')),
                ('padron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.padron')),
            ],
            options={
                'db_table': 'lotes',
            },
        ),
    ]
