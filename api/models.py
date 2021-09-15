from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    username = None
    nome = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome', )


class Local(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.TextField(null=False, blank=False)
    contato = models.CharField(max_length=11, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    imagem_local = models.ImageField(null=True, blank=False)
    usuario = models.OneToOneField(Usuario, related_name='usuario', on_delete=models.CASCADE)

class Objeto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    entregue = models.BooleanField(null=False, blank=False, default=False)
    imagem_objeto = models.ImageField(null=True, blank=False)
    local = models.ForeignKey(Local, related_name='objetos', on_delete=models.CASCADE)
    dono_nome = models.CharField(max_length=100, null=True, blank=True)
    dono_cpf = models.CharField(max_length=11, null=True, blank=True)





