#Usuarios
Lista_Usuarios = []
Lista_Identif = []
Ahorro = []
anterior=0

cont = 1
while cont == 1:
    print()
    print("Examen Final")
    print()

    print("Opcion 1. Creacion de un clientes")
    print("Opcion 2. Adicionar saldo")
    print("Opcion 3. Retirar Saldo")
    print("Opcion 4. Mostrar Saldo del usuario")
    print("Opcion 5. Mostrar saldo de todos los usuarios")
    print("Opcion 6. Cerrar aplicacion")

    Opcion=int(input("Selecione la opcion: ")) 
    i=0
    a=0
    if Opcion==1:
        Nombre = input(f'Usuario #{i+1} Digite su nombre para crear su cuenta: ')
        Lista_Usuarios.append(Nombre)
        resp=True
        seguir=True
        while resp or seguir:
            rep=0
            longitud=0
            try:
                Num_Doc=int(input(f'Usuario #{i+1} Digite su numero de identificacion: '))
                resp=False
                seguir=False
                if longitud==0:
                    Lista_Identif.append(Num_Doc)
                    longitud = len(Lista_Identif)
                    print("Cuenta creada correctamente")
                    Ahorro.append(0)
                else:
                    for rep in range(longitud):
                        if Lista_Identif[rep]==Num_Doc:
                            print("El número de identificación ya se encuentra registrado")
                            seguir = True
                        elif Lista_Identif[rep]!=Num_Doc:
                            Lista_Identif.append(Num_Doc)
                            longitud = len(Lista_Identif)
                            print("Cuenta creada correctamente")
                            Ahorro.append(0)
                    cont = 1
            except ValueError:
                print("ERROR, Tipo de caracter desconocido")   
    elif Opcion==2:
            user=int(input("Numero de identificacion: "))
            nuevo = Lista_Identif.index(user)
            if user==Lista_Identif[nuevo]:
                if user==Lista_Identif[nuevo] and Ahorro[nuevo]>=0:
                        print("Su total en cuenta es: $ {:,}".format(Ahorro[nuevo]).replace(',','~').replace('.',',').replace('~','.')) 
            if Lista_Identif[nuevo]==user:
                if user==Lista_Identif[nuevo] and Ahorro[nuevo]==0:
                    adicionar = int(input("Digite el total a guardar en el banco: "))
                    if adicionar>0:
                        Ahorro[nuevo]=adicionar
                        print("Guardado Correctamente")
                        cont = 1
                    elif adicionar<0:
                        adicionar=0
                        Ahorro[nuevo]=adicionar
                        print("No se ha Guardado")
                        cont = 1
                elif user==Lista_Identif[nuevo] and Ahorro[nuevo]>0:
                    adicionar = int(input("Digite el total a guardar en el banco: "))
                    if adicionar>0:
                        anterior = Ahorro[nuevo]+adicionar
                        Ahorro[nuevo]=anterior
                        print("Guardado Correctamente")
                        cont = 1
                    elif adicionar<0:
                        adicionar=0
                        anterior = Ahorro[nuevo]+adicionar
                        Ahorro[nuevo]=anterior
                        print("No se ha Guardado")
                        cont = 1                                           
    elif Opcion==3:
        user=int(input("Numero de identificacion: "))
        nuevo = Lista_Identif.index(user)
        if user==Lista_Identif[nuevo]:
            if user==Lista_Identif[nuevo] and Ahorro[nuevo]>0:
                    print("Su total en cuenta es: $ {:,}".format(Ahorro[nuevo]).replace(',','~').replace('.',',').replace('~','.')) 
        if Lista_Identif[nuevo]==user:
            if Ahorro[nuevo]==0:
                print("Usted no cuenta con dinero para retirar")
                cont = 1
            elif Ahorro[nuevo]>0:
                quitar = int(input("Digite la cantidad a retirar: "))
                if quitar>0 and Ahorro[nuevo]>=quitar:
                    anterior = Ahorro[nuevo]-quitar
                    Ahorro[nuevo]=anterior
                    print("Transacción realizada correctamente")
                    cont = 1
                elif quitar<0 or quitar>Ahorro[nuevo]:
                    quitar=0
                    anterior = Ahorro[nuevo]-quitar
                    Ahorro[nuevo]=anterior
                    print("Transacción no realizada")
                    cont = 1
    elif Opcion==4:
        user=int(input("Numero de identificacion: "))
        nuevo = Lista_Identif.index(user)
        if user==Lista_Identif[nuevo]:
            if user==Lista_Identif[nuevo] and Ahorro[nuevo]>=0:
                    print("Su total en cuenta es: $ {:,}".format(Ahorro[nuevo]).replace(',','~').replace('.',',').replace('~','.'))
        else:
            print("Este Usuario no existe, Intente mas tarde")
    elif Opcion==5:
        a=0
        while a<longitud:
            if Ahorro[a]>=0:
                print(f'Usuario {Lista_Usuarios[a]}'+" Su dinero en el banco es de: $ {:,}".format(Ahorro[a]).replace(',','~').replace('.',',').replace('~','.'))
            a=a+1
    elif Opcion==6:
        print("Gracias por preferirnos")
        exit()