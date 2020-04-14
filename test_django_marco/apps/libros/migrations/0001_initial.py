# Generated by Django 2.2.6 on 2019-10-03 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lectores', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('author', models.CharField(max_length=50, verbose_name='autor')),
                ('year', models.CharField(max_length=50, verbose_name='año')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectores.Lector')),
            ],
        ),
    ]