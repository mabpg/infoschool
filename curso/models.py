from django.db import models

class Curso (models.Model):

    CURSO = (
        ('Septimo', 'septimo'),
        ('Octavo', 'octavo'),
        ('Noveno', 'noveno'),
        ('Primero', 'primero'),
        ('Segundo', 'segundo'),
        ('Tercero', 'tercero'),
    )

    SECCION = (
        ('Primera', 'primera'),
        ('Segunda', 'segunda'),
        ('Tercera', 'tercera'),
        ('Cuarta', 'cuarta'),
    )

    TURNO = (
        ('Manana', 'manana'),
        ('Tarde', 'tarde'),
    )

    ESPECIALIDAD = (
        ('EEB', 'EEB'),
        ('Basica', 'basica'),
        ('Informatica', 'informatica'),
        ('Sociales', 'sociales'),
        ('Artes', 'artes'),
        ('Contabilidad', 'contabilidad'),
        ('Administracion', 'administracion'),
        ('Quimica', 'quimica'),
        ('Salud', 'salud'),
    )
    id_curso = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=18,
                              choices=CURSO,
                              default='Septimo')

    seccion = models.CharField(max_length=18,
                               choices=SECCION,
                               default='Primera')

    turno = models.CharField(max_length=18,
                             choices=TURNO,
                             default='Manana')

    especialidad = models.CharField(max_length=18,
                                    choices=ESPECIALIDAD,
                                    default='EEB')

    class Meta:
        db_table = 'curso'

    def __unicode__(self):
        return self.nombre
