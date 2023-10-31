import random
import string
import secrets
import datetime
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

    def demastricularse_curso(self,cursos_disponibles):
        if not self.mi_cursos:
            print("No estás matriculado en ningún curso.")
        else:
            print("Cursos en los que estás matriculado:")
            for i, curso in enumerate(self.mi_cursos, start=1):
                print(f"{i}. {curso.nombre}")
            opcion_curso = int(input("Seleccione el curso por ID: "))
            while opcion_curso < 1 or opcion_curso > len(cursos_disponibles):
                opcion_curso = int(input("Seleccione un número válido: "))

            curso_seleccionado = cursos_disponibles[opcion_curso - 1]

            print(f"Los cursos matriculados son nro: {curso_seleccionado}")

            contrasena_ingresada = input("Ingrese la contraseña de matriculación del curso: ")
            if contrasena_ingresada == curso_seleccionado.contrasena:
                # Elimina el curso seleccionado de la lista de cursos matriculados
                self.mi_cursos.remove(curso_seleccionado)
                print(f"Desmatriculación exitosa en el curso {curso_seleccionado.nombre}.")
            else:
                print("Error: Contraseña de matriculación incorrecta.")
        

    def ver_cursos_matriculados(self):
        if not self.mi_cursos:
            print("No estás matriculado en ningún curso.")
        else:
            print("Cursos en los que estás matriculado:")
            for i, curso in enumerate(self.mi_cursos, start=1):
                print(f"{i}. {curso.nombre}")
            opcion_curso = int(input("Seleccione el curso por ID para ver archivos: "))
            while opcion_curso < 1 or opcion_curso > len(self.mi_cursos):
                opcion_curso = int(input("Seleccione un número válido: "))

            curso_seleccionado = self.mi_cursos[opcion_curso - 1]
            if not curso_seleccionado.mi_archivo:
                print(f"No hay archivos en el curso {curso_seleccionado.nombre}")
            else:
                print(f"Archivos del curso {curso_seleccionado.nombre}:")
                for archivo in curso_seleccionado.mi_archivo:
                    print(f"Nombre: {archivo.nombre}")
                    print(f"Dato: {archivo.dato}")
                    print(f"Formato: {archivo.formato}")   

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, titulo, anio_recibido):
        super().__init__(nombre, apellido, email, contraseña)
        self.titulo = titulo
        self.anio_recibido = anio_recibido
        self.mis_cursos = []

    def dictar_curso(self):
        nombre_curso = input("Ingrese el nombre del curso a dictar: ")
        contrasena_matriculacion = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        nuevo_codigo_curso = secrets.randbelow(10000)

        nuevo_curso = Curso(nombre_curso, contrasena_matriculacion,nuevo_codigo_curso)
        self.mis_cursos.append(nuevo_curso)
        cursos_disponibles.append(nuevo_curso)
        print("Curso dado de alta con éxito.")
        print(f"Nombre: {nuevo_curso.nombre}")
        print(f"Contraseña: {nuevo_curso.contrasena}")
        print(f"Contraseña: {nuevo_curso.codigo}")

    def ver_cursos(self):
        if not self.mis_cursos:
            print("No tienes cursos dictados.")
        else:
            print("Cursos que dictas:")
            for i, curso in enumerate(self.mis_cursos, start=1):
                print(f"{i} {curso.nombre}")
                while True:
                    opcion_curso = input("Seleccione el curso por ID para ver detalles (0 para salir): ")
                    if opcion_curso == '0':
                        break

                    try:
                        opcion_curso = int(opcion_curso)
                        if opcion_curso < 1 or opcion_curso > len(self.mis_cursos):
                            print("Seleccione un número válido.")
                            continue
                    except ValueError:
                        print("Por favor, ingresa un número válido.")
                        continue

                    curso_seleccionado = self.mis_cursos[opcion_curso - 1]
                    print(f"Nombre: {curso_seleccionado.nombre}")
                    print(f"Código: {curso_seleccionado.codigo}")
                    print(f"Contraseña: {curso_seleccionado.contrasena}")
                    print(f"Cantidad de archivos: {len(curso_seleccionado.mi_archivo)}")

                    agregar_archivo = int(input("¿Deseas agregar un archivo adjunto? (1=Sí/2=No): "))
                    if agregar_archivo == 1:
                        nombre_archivo = input("Ingrese el nombre del archivo: ")
                        formato_archivo = input("Ingrese el formato del archivo: ")
                        fecha_hoy = datetime.date.today()
                        nuevo_archivo = Archivo(nombre_archivo,nombre_archivo,formato_archivo)
                        curso_seleccionado.agregar_archivo(nuevo_archivo)
                        print("Archivo agregado con éxito.")

class Curso:
    def __init__(self, nombre, contrasena,codigo, mi_archivo=None):
        self.nombre = nombre
        self.contrasena = contrasena
        self.codigo = codigo
        self.mi_archivo = mi_archivo if mi_archivo is not None else []

    def agregar_archivo(self, archivo):
        self.mi_archivo.append(archivo) 

class Carrera(Curso):
    def __init__(self, codigo, nombre, nombre_carrera):
        super().__init__(codigo, nombre)
        self.nombre_carrera = nombre_carrera

class Archivo:
    def  __init__(self, nombre,dato,formato):
        self.nombre = nombre
        self.dato = dato
        self.formato = formato




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
archivos = [
    Archivo("pepe","cosas","pdf"),
    Archivo ("micasa","dos cosas","php"),
]

cursos_disponibles = [
    Curso("Programación I", "123456",4),
    Curso("Estadisitica", "789012",5),
    Curso("Laboratorio","334455",6)
]

cursos_disponibles[0].mi_archivo.append(archivos[0])
cursos_disponibles[0].mi_archivo.append(archivos[1])

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
                print("2. Desmatricularse de un curso")
                print("3. Ver cursos matriculados")
                print("4. Volver al menú principal")
                
                opcion_alumno = input("Elija una opción: ")

                if opcion_alumno == "1":
                    alumno_encontrado.matricularse_a_curso(cursos_disponibles)
                elif opcion_alumno == "2":
                    alumno_encontrado.demastricularse_curso(cursos_disponibles)
                elif opcion_alumno == "3":
                    alumno_encontrado.ver_cursos_matriculados()
                elif opcion_alumno == "4":
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
       
        cursos_disponibles_sorted = sorted(cursos_disponibles, key=lambda x: x.nombre)
        print("Cursos disponibles:")
        for i, curso in enumerate(cursos_disponibles_sorted, start=1):
            print(f"{i}. {curso.nombre}")
            
    elif op2 == 4:
        print("Hasta luego")
        op1 = 4
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

    op1 = int(input("Ingrese 1 si quiere continuar: "))

    