# Generated by Django 3.1.6 on 2021-03-11 06:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('rua', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(default='Sem número', max_length=6)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Cliente ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=155)),
                ('cpf', models.CharField(blank=True, max_length=155, null=True)),
                ('telefone', models.CharField(max_length=13, null=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.endereco')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
