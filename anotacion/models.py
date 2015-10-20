import datetime
from django.db import models
from materia.models import Materia
from curso.models import Curso


class Anotacion (models.Model):

    id_anotacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    curso = models.ForeignKey(Curso, null=True, blank=True)
    materia = models.ForeignKey(Materia, null=True, blank=True)
    fecha = models.DateTimeField(default= datetime.datetime.now())

    class Meta:
        db_table = 'anotacion'

    def __unicode__(self):
        return self.nombre
