from django.db import models

class Alumno (models.Model):

    id_alumno = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)

    fecha_nacimiento = models.DateField(null=False)

    ##curso = models.ForeignKey(Curso, blank=False, null=False)
    #padre = models.ForeignKey(Padre)
    #madre = models.ForeignKey(Padre)

    class Meta:
        db_table = 'alumno'

    def __unicode__(self):
        return self.fecha_nacimiento        #cambiar aca este campo
