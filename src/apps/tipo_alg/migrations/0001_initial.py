# Generated by Django 4.0.5 on 2022-07-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Alg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_cosecha', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_alg',
            },
        ),
    ]
