from django.db import models

# Create your models here.

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.titulo