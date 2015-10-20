from django.db import models
from usuario.models import Usuario
from curso.models import Curso

class Alumno (models.Model):

    id_alumno = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)

    fecha_nacimiento = models.DateTimeField(null=False)

    curso = models.ForeignKey(Curso, blank=True, null=True)
    #padre = models.ForeignKey(Padre)
    #madre = models.ForeignKey(Padre)

    class Meta:
        db_table = 'alumno'

    def __unicode__(self):
        return self.usuario.nombre        #cambiar aca este campo



""" class CursoAlumno (models.Model):

    id_curso_alumno = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, blank=True, null=True)
    alumno = models.ForeignKey(Alumno, blank=True, null=True)

    class Meta:
        db_table = 'curso_alumno'

    def __unicode__(self):
        return self.curso"""