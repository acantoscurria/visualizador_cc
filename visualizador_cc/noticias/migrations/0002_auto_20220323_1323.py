# Generated by Django 3.2.12 on 2022-03-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen1',
            field=models.ImageField(null=True, upload_to='static/images/noticias', verbose_name='Imagen 1'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen2',
            field=models.ImageField(null=True, upload_to='static/images/noticias', verbose_name='Imagen 2'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen3',
            field=models.ImageField(null=True, upload_to='static/images/noticias', verbose_name='Imagen 3'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen4',
            field=models.ImageField(null=True, upload_to='static/images/noticias', verbose_name='Imagen 4'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen5',
            field=models.ImageField(null=True, upload_to='static/images/noticias', verbose_name='Imagen 5'),
        ),
    ]
