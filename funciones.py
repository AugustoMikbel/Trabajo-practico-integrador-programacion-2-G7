class Alumno:
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

alumnos_datos = [
    Alumno("Pepe", "Martinez", "pmarto@gmail.com", "pemart"),
    Alumno("Jose", "Leonidas", "joseleo@gmail.com", "jose123"),
    Alumno("Norman", "Aurelio", "anorman@gmail.com", "anorman"),
]

def alumnos():
    email = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")

    alumno_encontrado = None
    for alumno in alumnos_datos:
        if alumno.email == email and alumno.contraseña == contraseña:
            alumno_encontrado = alumno
            break

    if alumno_encontrado != None:
        print(f"Bienvenido, {alumno_encontrado.nombre} {alumno_encontrado.apellido}")
        menualumnos()
    else:
        print("El correo o la contraseña son incorrectos.Porfavor hable con alumnado, gracias")


def menualumnos():

    print("1_ Matricularse a un curso")
    print("2_Ver curso")
    print("3_Volver al menu principal")
    op3=int(input("Que desea: "))
    while (op3>=4 or op3<=0):
            op3=int(input("escriba el nro de vuelta entre el 1 y el 3: "))
    if(op3==1):
         print("op1")
    elif(op3==2):
         print("op2")

    elif(op3==3):   
         print("op3") 