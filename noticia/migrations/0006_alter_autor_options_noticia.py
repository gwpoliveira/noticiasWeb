# Generated by Django 4.2.6 on 2023-11-09 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0005_autor_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Escritor', 'verbose_name_plural': 'Escritores'},
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('conteudo', models.TextField(verbose_name='Conteudo')),
                ('data_pub', models.DateField(verbose_name='Data da publicação')),
                ('tags', models.CharField(choices=[('Urgente', 'Urgene'), ('Esporte', 'Esporte'), ('Politica', 'Politica')], max_length=100, verbose_name='Categoria')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticia.autor', verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
