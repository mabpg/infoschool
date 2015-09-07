from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)


class Usuario (AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, unique=True)
    apellido = models.CharField(max_length=30, blank=False)

    USERNAME_FIELD = 'nombre'

    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = 'usuario'