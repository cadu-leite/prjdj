# Generated by Django 2.2.6 on 2019-10-09 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emissor',
            fields=[
                ('cpnj', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='CNPJ')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_nota_fiscal', models.CharField(blank=True, max_length=50, null=True, verbose_name='numero da nota fiscal')),
                ('receita_despesa', models.PositiveSmallIntegerField(choices=[(1, 'despesa'), (2, 'receita')], verbose_name='receita ou despesa')),
                ('valor_nota', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('emissor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Emissor')),
            ],
            options={
                'verbose_name': 'Lançamento',
                'verbose_name_plural': 'Lançamentos',
            },
        ),
    ]
