from django.db import models
from usuario.models import Usuario

class Alumno (models.Model):

    id_alumno = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, blank=False, null=False)

    fecha_nacimiento = models.DateTimeField(null=False)

    ##curso = models.ForeignKey(Curso, blank=False, null=False)
    #padre = models.ForeignKey(Padre)
    #madre = models.ForeignKey(Padre)

    class Meta:
        db_table = 'alumno'

    def __unicode__(self):
        return self.id_alumno        #cambiar aca este campo
