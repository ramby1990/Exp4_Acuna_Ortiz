# Generated by Django 4.0.4 on 2022-06-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
