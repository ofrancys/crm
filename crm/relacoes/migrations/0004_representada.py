# Generated by Django 4.1.7 on 2024-05-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacoes', '0003_alter_produto_descricao_alter_produto_medida_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18)),
                ('razao', models.CharField(max_length=96)),
                ('contato', models.CharField(max_length=96)),
                ('numero', models.FloatField(max_length=18)),
                ('endereco', models.CharField(max_length=96)),
            ],
        ),
    ]
