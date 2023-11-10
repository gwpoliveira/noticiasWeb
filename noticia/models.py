from django.db import models

# Create your models here.

class Autor(models.Model):
    
    nome = models.CharField("Nome",max_length=200, blank= True)
    data_nascimento = models.DateField('Data de Nascimento',default="1980-01-01")
    email = models.EmailField('Email:', blank= True, null=True)
    idade = models.PositiveSmallIntegerField('Idade')
    avatar = models.ImageField('Foto',upload_to="avatares", blank=True, null= True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Escritor'
        verbose_name_plural = 'Escritores'
    
    
class Noticia(models.Model):
    
    CATEGORIAS = [
        ('Urgente','Urgene'),
        ('Esporte','Esporte'),
        ('Politica','Politica'),
        
    ]
    
    titulo = models.CharField('Titulo',max_length=200, blank= True)
    conteudo = models.TextField('Conteudo', blank= True)
    data_pub = models.DateField('Data da publicação', blank= True, null=True)
    tags = models.CharField('Categoria', max_length=100, choices=CATEGORIAS)
    autor = models.ForeignKey(Autor, verbose_name="Autor", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'