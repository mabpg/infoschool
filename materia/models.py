from django.db import models
from usuario.models import Usuario
from curso.models import Curso

class Materia (models.Model):

    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False)
    profesor = models.ForeignKey(Usuario, null=True, blank=True)

    class Meta:
        db_table = 'materia'

    def __unicode__(self):
        return self.nombre


class Materia_curso (models.Model):

    id_materia_curso = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, null=True, blank=True)
    materia = models.ForeignKey(Materia, null=True, blank=True)

    class Meta:
        db_table = 'materia_curso'

    def __unicode__(self):
        return self.curso.nombre