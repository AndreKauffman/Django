# Generated by Django 3.1.7 on 2021-03-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contas', '0002_transação'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transação',
            options={'verbose_name_plural': 'Transações'},
        ),
        migrations.AlterField(
            model_name='transação',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transação',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
