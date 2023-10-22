import datos as da


def alumnos():
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")

    if email in da.alumnos["gmaila"]:
        index = da.alumnos["gmaila"].index(email)
        if da.alumnos["contraa"][index] == password:
            print(f"Bienvenido, {da.alumnos['nombrea'][index]} {da.alumnos['apellidoa'][index]}")
            menualumnos()
        else:
            print("Error: La contraseña ingresada es incorrecta.")
    else:
        print("El correo electrónico no está registrado. Debe darse de alta en alumnado.")


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