from django.db import models

# Create your models here.
class Arte(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    idartista = models.IntegerField('Nome', max_length=5)
    idvalor = models.IntegerField('Nome', max_length=5)
    idhistoria = models.IntegerField('Nome', max_length=5)
    idcategoria = models.IntegerField('Nome', max_length=5)
    url = models.CharField('URL', max_length=200)
    description = models.TextField('Descricao', max_length=100) 

    
    class Meta:
        verbose_name = 'Arte'
        verbose_name_plural = 'Artes'
        ordering =['id']

    def __str__(self):
        return self.name
