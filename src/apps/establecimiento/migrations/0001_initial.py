# Generated by Django 4.0.5 on 2022-07-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('padron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('codigo_establecimiento', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('descripcion_establecimiento', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=20)),
                ('departamento', models.CharField(max_length=20)),
                ('padron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padron.padron')),
            ],
            options={
                'db_table': 'establecimiento',
            },
        ),
    ]
