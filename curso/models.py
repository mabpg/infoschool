from django.db import models

class Curso (models.Model):

    id_curso = models.AutoField(primary_key=True)

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
    nombre = models.CharField(max_length=15, choices=CURSO, default='Septimo')
    seccion = models.CharField(max_length=15, choices=SECCION, default='Primera')
    turno = models.CharField(max_length=10, choiches=TURNO, default='Manana')
    especialidad = models.CharField(max_length=10, choiches=ESPECIALIDAD, default='Basica')


    class Meta:
        db_table = 'curso'

    def __unicode__(self):
        return self.nombre
