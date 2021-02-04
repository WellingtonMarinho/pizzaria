# Generated by Django 3.1.6 on 2021-02-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='tamanho',
            field=models.CharField(choices=[(1, 'Pequeno'), (2, 'Médio'), (3, 'Grande')], default='Médio', max_length=10),
            preserve_default=False,
        ),
    ]
