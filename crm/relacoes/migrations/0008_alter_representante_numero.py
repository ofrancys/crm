# Generated by Django 4.1.7 on 2024-06-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacoes', '0007_alter_representante_cnpj_alter_representante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representante',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
