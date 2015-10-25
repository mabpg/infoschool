import datetime
from django.db import models
from materia.models import Materia
from curso.models import Curso
from alumno.models import Alumno

class Anotacion (models.Model):

    id_anotacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    alumno = models.ForeignKey(Alumno,null=True, blank=True)
    descripcion = models.CharField(max_length=45, null=True, blank=True)
    materia = models.ForeignKey(Materia, null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    responsable = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'anotacion'

    def __unicode__(self):
        return self.nombre
