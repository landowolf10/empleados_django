# Generated by Django 3.0.3 on 2020-08-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentomodel',
            name='short_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
