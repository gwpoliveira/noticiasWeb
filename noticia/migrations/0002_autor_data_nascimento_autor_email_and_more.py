# Generated by Django 4.2.5 on 2023-09-14 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='data_Nascimento',
            field=models.DateField(default='1978-01-01'),
        ),
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.EmailField(default='exemplo@com.br', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome_Autor',
            field=models.CharField(max_length=200),
        ),
    ]
