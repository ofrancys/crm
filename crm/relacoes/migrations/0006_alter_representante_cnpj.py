# Generated by Django 4.1.7 on 2024-06-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacoes', '0005_representante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representante',
            name='cnpj',
            field=models.IntegerField(max_length=18),
        ),
    ]
