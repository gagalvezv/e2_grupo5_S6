# Generated by Django 5.0.3 on 2024-04-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_usuario_apellidos_remove_usuario_nombres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=25, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=25, verbose_name='nombres'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=20, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='rut'),
        ),
    ]
