import random
import string
class Usuario:
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña



class Alumno(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, legajo, año_matriculacion):
        super().__init__(nombre, apellido, email, contraseña)
        self.legajo = legajo
        self.año_matriculacion = año_matriculacion
        self.mi_cursos = []

    def matricularse_a_curso(self, cursos_disponibles):
        print("Cursos disponibles para matricularse:")
        for i, curso in enumerate(cursos_disponibles, start=1):
            print(f"{i}. {curso.nombre}")

        opcion_curso = int(input("Seleccione el curso por ID: "))
        while opcion_curso < 1 or opcion_curso > len(cursos_disponibles):
            opcion_curso = int(input("Seleccione un número válido: "))

        curso_seleccionado = cursos_disponibles[opcion_curso - 1]

        if curso_seleccionado in self.mi_cursos:
            print("Ya estás matriculado en este curso.")
        else:
            contrasena_ingresada = input("Ingrese la contraseña de matriculación del curso: ")
            if contrasena_ingresada == curso_seleccionado.contrasena:
                self.mi_cursos.append(curso_seleccionado)
                print(f"Matriculación exitosa en el curso {curso_seleccionado.nombre}.")
            else:
                print("Error: Contraseña de matriculación incorrecta.")

    def ver_cursos_matriculados(self):
        if not self.mi_cursos:
            print("No estás matriculado en ningún curso.")
        else:
            print("Cursos en los que estás matriculado:")
            for i, curso in enumerate(self.mi_cursos, start=1):
                print(f"{i}. {curso.nombre}")

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, titulo, anio_recibido):
        super().__init__(nombre, apellido, email, contraseña)
        self.titulo = titulo
        self.anio_recibido = anio_recibido
        self.mis_cursos = []

    def dictar_curso(self):
        nombre_curso = input("Ingrese el nombre del curso a dictar: ")
        contrasena_matriculacion = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

        nuevo_curso = Curso(nombre_curso, contrasena_matriculacion)
        self.mis_cursos.append(nuevo_curso)
        cursos_disponibles.append(nuevo_curso)
        print("Curso dado de alta con éxito.")
        print(f"Nombre: {nuevo_curso.nombre}")
        print(f"Contraseña: {nuevo_curso.contrasena}")

    def ver_cursos(self):
        if not self.mis_cursos:
            print("No tienes cursos dictados.")
        else:
            print("Cursos que dictas:")
            for i, curso in enumerate(self.mis_cursos, start=1):
                print(f"{i} {curso.nombre}")
class Curso:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

class Archivo:

# Inicialización de datos
alumnos_datos = [
    Alumno("Pepe", "Martinez", "pmarto@gmail.com", "pemart", "12345", 2020),
    Alumno("Jose", "Leonidas", "joseleo@gmail.com", "jose123", "54321", 2021),
]

profesor_datos = [
    Profesor("Martin", "Lopez", "martin@g.com", "martin123", "Doctor", 2005),
    Profesor("Mariela", "Viloni", "mariela@g.com", "mar123", "Ingeniera", 2002),
    Profesor("Augusto", "Sánchez", "augus@g.com", "augus123", "Licenciado", 2004),

]

cursos_disponibles = [
    Curso("Programación I", "123456"),
    Curso("Estadisitica", "789012"),
    Curso("Laboratorio","334455")
]
op1 = 1

while op1 == 1:
    print("Menú Principal")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    
    op2 = int(input("¿Qué desea?: "))
    while op2 >= 5 or op2 <= 0:
        op2 = int(input("Escriba el número de vuelta entre el 1 y el 4: "))

    if op2 == 1:
        email = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")
        
        alumno_encontrado = None
        for alumno in alumnos_datos:
            if alumno.email == email and alumno.contraseña == contraseña:
                alumno_encontrado = alumno
                break

        if alumno_encontrado:
            print(f"Bienvenido, {alumno_encontrado.nombre}")
            while True:
                print("Sub Menú Alumno")
                print("1. Matricularse a un curso")
                print("2. Ver cursos matriculados")
                print("3. Volver al menú principal")
                
                opcion_alumno = input("Elija una opción: ")

                if opcion_alumno == "1":
                    alumno_encontrado.matricularse_a_curso(cursos_disponibles)
                elif opcion_alumno == "2":
                    alumno_encontrado.ver_cursos_matriculados()
                elif opcion_alumno == "3":
                    break
        else:
            print("El correo o la contraseña son incorrectos. Por favor hable con alumnado, gracias")
        pass
    elif op2 == 2:
        # Código para ingresar como profesor
        email = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")
        
        Profesor_encontrado = None
        for profesor in profesor_datos:
            if profesor.email == email and profesor.contraseña == contraseña:
                profesor_encontrado = profesor
                break

        if profesor_encontrado:
            print(f"Bienvenido, {profesor_encontrado.nombre}")
            while True:
                print("Sub Menú Profesor")
                print("1. Dictar curso")
                print("2. Ver cursos")
                print("3. Volver al menú principal")
                
                opcion_profesor = input("Elija una opción: ")

                if opcion_profesor == "1":
                    profesor_encontrado.dictar_curso()
                elif opcion_profesor == "2":
                    profesor_encontrado.ver_cursos()
                elif opcion_profesor == "3":
                    break
        else:
            print("El correo o la contraseña son incorrectos. Por favor hable con alumnado, gracias")
        pass
    elif op2 == 3:
        print("Cursos disponibles:")
        for i, curso in enumerate(cursos_disponibles, start=1):
            print(f"{i}. {curso.nombre}")
            pass
    elif op2 == 4:
        print("Hasta luego")
        op1 = 4
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

    op1 = int(input("Ingrese 1 si quiere continuar: "))