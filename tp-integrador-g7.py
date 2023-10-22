import funciones as fun

op1=1

while(op1==1):
    print("1_Ingresar como alumno")
    print("2_Ingresar como estudiante")
    print("3_Ver cursos")
    print("4_Salir")

    op2=int(input("Que desea: "))
    while (op2>=5 or op2<=0):
            op2=int(input("escriba el nro de vuelta entre el 1 y el 4: "))


    if(op2 == 1):
        print("opcion alumno")
        fun.alumnos()
    elif(op2 == 2):
        print("opcion maestro")

    elif(op2 == 3):
        print("ver curso")

    elif(op2==4):
        print("chau")    
    op1=int(input ("ingrese 1 si quiere continuar: "))

