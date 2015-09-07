"""Prueba de Autenticacion
    Este test devuelve OK en el caso que no ocurran errores,
"""

from django.test import TestCase, Client

from usuario.models import Usuario


class TestLogin(TestCase):
    """
    TestLogin
        Se define un persona para iniciar nuestro test.
        Completamos los campos requeridos con los siguientes valores:
            username: prueba
            email: test@test.com
            password: prueba
    """

    def setUp(self):
        self.client = Client()
        self.nombre_usuario= 'prueba'
        self.correo_electronico= 'test@test.com'
        self.password = 'prueba'
        self.test_user = Usuario.objects.create_user(self.nombre_usuario, self.password)

    """ test_login_exitoso
        Con el usuario creado (username y password correctos) probamos si se loguea correctamente
    """

    def test_login_exitoso(self):
        login = self.client.login(nombre_usuario=self.nombre_usuario, password=self.password)
        self.assertEqual(login, True, 'el sistema de login no esta funcionando correctamente')
        print('ejecutando test 1 login exitoso')

    """ test_usuario_incorrecto
        Se prueba un usuario incorrecto con el password del usuario 'prueba' creado recientemente
    """

    def test_usuario_incorrecto(self):
        login = self.client.login(nombre_usuario='ola que ase', password=self.password)
        self.assertEqual(login, False, 'un usuario incorrecto realizo un login')
        print('ejecutando test 2 usuario incorrecto')

    """ test_password_incorrecto
        Se prueba un usuario correcto con el password incorrecto
    """
    def test_password_incorrecto(self):
        login = self.client.login(nombre_usuario=self.nombre_usuario, password='ola que ase password')
        self.assertEqual(login, False, 'un password incorrecto realizo un login')
        print('ejecutando test 3 password incorrecto')
    """ test_usuario_vacio
        Se prueba un usuario vacio con el password del usuario 'prueba' creado recientemente
    """

    def test_usuario_vacio(self):
        login = self.client.login(nombre_usuario='', password=self.password)
        self.assertEqual(login, False, 'un usuario vacio realizo un login')
        print('ejecutando test 4 usuario vacio')

    """ test_password_vacio
        Probamos con el usuario correcto con el password vacio
    """
    def test_password_vacio(self):
        login = self.client.login(nombre_usuario=self.nombre_usuario, password='')
        self.assertEqual(login, False, 'Un password vacio realizo un login')
        print('ejecutando test 5 password vacio')


"""
class RolTestCase(TestCase):
    rol1=None
    permiso1=None
    usuario_rol_proyecto=None
    def asignar_roles(self):
        usuario1=Usuario.objects.create_user('Homero', '12345')
        usuario2=Usuario.objects.create_user('Cristina', '12345')
        self.rol1=Rol.objects.create(nombre='Rol1', fecha_creacion='2015-04-22', descripcion=" LOL ", tipo='Proyecto')
        self.permiso1=PermisoProyecto.objects.create(crear_flujo=True,modificar_flujo=True)

        self.usuario_rol_proyecto= Usuario_Rol_Proyecto(id_usuario= usuario1, id_roles=self.rol1, id_permiso_proyecto=self.permiso1)
        self.usuario_rol_proyecto.id_usuario.add(usuario2)
"""
