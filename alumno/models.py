from django.db import models

class Alumno (models.Model):

    id_alumno = models.AutoField(primary_key=True)
    #usuario = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(null=False)
    fecha_nacimiento = models.DateField(null=False)
    direccion = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    ##curso = models.ForeignKey(Curso, blank=False, null=False)
    #padre = models.ForeignKey(Padre)
    #madre = models.ForeignKey(Padre)

    class Meta:
        db_table = 'alumno'

    def __unicode__(self):
        return self.edad        #cambiar aca este campo
