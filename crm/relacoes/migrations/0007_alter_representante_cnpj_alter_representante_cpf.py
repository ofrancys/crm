# Generated by Django 4.1.7 on 2024-06-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacoes', '0006_alter_representante_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representante',
            name='cnpj',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='representante',
            name='cpf',
            field=models.IntegerField(),
        ),
    ]