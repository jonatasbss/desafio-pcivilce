# Generated by Django 4.0.4 on 2022-05-11 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armas', '0002_arma_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arma',
            options={'ordering': ['marca_armamento']},
        ),
        migrations.AlterModelOptions(
            name='municao',
            options={'ordering': ['marca_municao']},
        ),
        migrations.RenameField(
            model_name='arma',
            old_name='marca',
            new_name='marca_armamento',
        ),
        migrations.RenameField(
            model_name='municao',
            old_name='marca',
            new_name='marca_municao',
        ),
    ]
