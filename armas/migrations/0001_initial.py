# Generated by Django 4.0.4 on 2022-05-10 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_calibre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'calibre',
            },
        ),
        migrations.CreateModel(
            name='ObjetoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_objeto', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'objeto_tipo',
            },
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armas.objetotipo')),
            ],
            options={
                'db_table': 'objeto',
            },
        ),
        migrations.CreateModel(
            name='Municao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, max_length=64, null=True)),
                ('modelo_municao', models.CharField(blank=True, max_length=64, null=True)),
                ('valor_estimado_municao', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('calibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calibre_municao', to='armas.calibre')),
            ],
            options={
                'db_table': 'municao',
                'ordering': ['marca'],
            },
        ),
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, max_length=64, null=True)),
                ('modelo_armamento', models.CharField(blank=True, max_length=64, null=True)),
                ('quantidade_de_tiros', models.IntegerField(blank=True, null=True)),
                ('valor_estimado_armamento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('calibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calibre_arma', to='armas.calibre')),
            ],
            options={
                'db_table': 'arma',
                'ordering': ['marca'],
            },
        ),
    ]
