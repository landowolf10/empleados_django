# Generated by Django 3.1 on 2020-08-26 00:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleadomodel_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleadomodel',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='Text'),
            preserve_default=False,
        ),
    ]