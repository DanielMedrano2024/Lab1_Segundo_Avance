# Generated by Django 5.1.2 on 2024-11-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=110)),
                ('telefono', models.IntegerField()),
                ('hora', models.TimeField()),
                ('ampm', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2)),
                ('servicio', models.CharField(choices=[('consulta', 'Consulta'), ('seguimiento', 'Seguimiento'), ('evaluacion', 'Evaluación')], max_length=20)),
            ],
        ),
    ]
