# Generated by Django 4.0.1 on 2022-01-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='redendimento',
            field=models.CharField(max_length=50),
        ),
    ]