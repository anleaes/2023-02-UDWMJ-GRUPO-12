from django.db import models

# Create your models here.
class Artista(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    idade = models.TextField('Idade', max_length=2)
    nascionalidade = models.TextField('Nascionalidade', max_length=50) 
    
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.name
