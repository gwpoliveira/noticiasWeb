# Generated by Django 4.2.6 on 2023-11-28 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0007_alter_autor_avatar_alter_autor_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'permissions': [('pode_publicar', 'Pode publicar uma noticia')], 'verbose_name': 'Escritor', 'verbose_name_plural': 'Escritores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='conteudo',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_pub',
            field=models.DateField(verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='tags',
            field=models.CharField(choices=[('Urgente', 'Urgente'), ('Esportes', 'Esportes'), ('Política', 'Política')], max_length=100, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
