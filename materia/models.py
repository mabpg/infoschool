from django.db import models
from usuario.models import Usuario

class Materia (models.Model):

    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False)
    profesor = models.ForeignKey(Usuario, null=True, blank=True)


    class Meta:
        db_table = 'materia'

    def __unicode__(self):
        return self.nombre        #cambiar aca este campo
