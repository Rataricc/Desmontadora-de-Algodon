# Generated by Django 4.0.5 on 2022-07-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padron', '0003_lotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotes',
            name='numero_lote',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=5),
        ),
    ]
