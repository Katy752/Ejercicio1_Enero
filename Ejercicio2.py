class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    def __init__(self, nombre, edad, calificacion):
        Persona.__init__(self, nombre, edad)
        self.calificacion = calificacion

    def mostrar_informacion(self):
        print('El alumno se llama: ' + self.nombre)
        print('La edad es: ' + str(self.edad))
        print('Su calificacion es: ' + str(self.calificacion))

    def cargar_calificacion(self):
        print('Ingresar calificacion de ' + self.nombre + ':')
        self.calificacion = input()


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

    def mostrar_informacion(self):
        print('El empleado se llama: ' + self.nombre)
        print('Su edad es: ' + str(self.edad))
        print('Su Sueldo es: ' + str(self.sueldo))


print('Ingresar nombre del alumno:')
nombre = input()
print('Ingresar edad del alumno:')
edad = input()
print('Ingresar calificacion del alumno:')
calificacion = input()
nuevo_alumno = Alumno(nombre, edad, calificacion)
nuevo_alumno.mostrar_informacion()

print('Ingresar nombre del empleado:')
nombre = input()
print('Ingresar edad del empleado:')
edad = input()
print('Ingresar sueldo del empleado:')
sueldo = input()
nuevo_empleado = Empleado(nombre, edad, sueldo)
nuevo_empleado.mostrar_informacion()
