Productos = []
Codigos_Pro = []
Cant_Pro = []
costo_unitario = []
Modificaciones=0

continuar = 1
while continuar == 1:
    print("1. Crear producto")
    print("2. Modificar producto")
    print("3. Mostrar producto")
    print("4. Agregar Cantidad")
    print("5. Sacar Cantidad")
    print("6. Salir")


    Opcion=int(input("Selecionar solamente una opcion: ")) 
    i=0
    a=0
    if Opcion==1:
        Producto = input("Nombre del producto: ")
        Productos.append(Producto)
        Respuesta=True
        seguir=True
        while Respuesta or seguir:
            rep=0
            Inventario=0
            try:
                Codigo=input("Codigo del producto: ")
                Respuesta=False
                seguir=False
                if Inventario==0:
                    Codigos_Pro.append(Codigo)
                    Inventario = len(Codigos_Pro)
                    print("Producto añadido correctamente")
                    costo_unitario.append(0)
                else:
                    for rep in range(Inventario):
                        if Codigos_Pro[rep]==Codigo:
                            print("Este codigo ya se encuentra asignado a un Producto ")
                            seguir = True
                        elif Codigos_Pro[rep]!=Codigo:
                            Codigos_Pro.append(Codigo)
                            Inventario = len(Codigos_Pro)
                            print("Producto añadido correctamente")
                            costo_unitario.append(0)
                    continuar = 1
            except ValueError:
                print("ERROR, Intente nuevamente")
        Cantidad_Pro = int(input("Cantidad de este producto: "))
        Cant_Pro.append(Cantidad_Pro)   
    elif Opcion==2:
            Cod_Pro=input("Codigo del producto: ")
            Posiciones = Codigos_Pro.index(Cod_Pro)
            if Cod_Pro==Codigos_Pro[Posiciones]:
                if Cod_Pro==Codigos_Pro[Posiciones] and costo_unitario[Posiciones]>=0:
                        print("")
                        print(f'Nombre del producto: {Productos[Posiciones]}') 
                        print("Valor Unitario del producto ${:,}".format(costo_unitario[Posiciones]).replace(',','~').replace('.',',').replace('~','.')) 
                        print(f'Cantidad: {Cant_Pro[Posiciones]} Unidades')
                        print("")
                if Cod_Pro==Codigos_Pro[Posiciones]: 
                    print("1. Modificar codigo del producto \n"+"2. Modificar nombre del producto \n"+"3. Modificar valor del producto \n"+"4. Modificar cantidad \n"+"5. Modificar Todos los datos")
                    op = int(input("Digite una opcion: "))
                    if op==1:
                        Codigo=input("Nuevo codigo del producto: ")
                        Codigos_Pro[Posiciones]=Codigo
                    elif op==2:
                        Producto = input("Nombre del producto: ")
                        Productos[Posiciones]=Producto
                    elif op==3:
                        Costo = int(input("Valor Unitario del producto: "))
                        costo_unitario[Posiciones]=Costo
                        if Costo>0:
                            costo_unitario[Posiciones]=Costo
                            print("Guardado Correctamente")
                            continuar = 1
                        elif Costo<0:
                            Costo=0
                            costo_unitario[Posiciones]=Costo
                            print("No se ha Guardado")
                            continuar = 1
                    elif op==4:
                        Cantidad_Pro = int(input("Cantidad de este producto: "))
                        Cant_Pro[Posiciones]=Cantidad_Pro
                    elif op==5:
                        Codigo=input("Nuevo codigo del producto: ")
                        Codigos_Pro[Posiciones]=Codigo
                        Producto = input("Nombre del producto: ")
                        Productos[Posiciones]=Producto
                        Costo = int(input("Valor Unitario del producto: "))
                        costo_unitario[Posiciones]=Costo
                        if Costo>0:
                            costo_unitario[Posiciones]=Costo
                            print("Guardado Correctamente")
                            continuar = 1
                        elif Costo<0:
                            Costo=0
                            costo_unitario[Posiciones]=Costo
                            print("No se ha Guardado")
                            continuar = 1
                        Cantidad_Pro = int(input("Cantidad de este producto: "))
                        Cant_Pro[Posiciones]=Cantidad_Pro
            else:
                print("Ese codigo de producto no existe")                                         
    elif Opcion==3:
        Cod_Pro=input("Codigo del producto: ")
        Posiciones = Codigos_Pro.index(Cod_Pro)
        if Cod_Pro==Codigos_Pro[Posiciones]:
                print("")
                print(f'Nombre del producto: {Productos[Posiciones]}')
                print(f'Cantidad del producto: {Cant_Pro[Posiciones]}')
                print("Valor Unitario: ${:,}".format(costo_unitario[Posiciones]).replace(',','~').replace('.',',').replace('~','.'))
                print("")
        else:
            print("Este codido no existe, Intente mas tarde")
    elif Opcion==4:
        Cod_Pro=input("Codigo del producto: ")
        Posiciones = Codigos_Pro.index(Cod_Pro)
        if Cod_Pro==Codigos_Pro[Posiciones]:
                print("")
                print(f'Nombre del producto: {Productos[Posiciones]}') 
                print("Valor Unitario del producto ${:,}".format(costo_unitario[Posiciones]).replace(',','~').replace('.',',').replace('~','.')) 
                print(f'Cantidad: {Cant_Pro[Posiciones]} Unidades')
                print("")
        else:
            print("Incorrecto, intente mas tarde")        
        if Codigos_Pro[Posiciones]==Cod_Pro:
            if Cant_Pro[Posiciones]>=0:
                agregar = int(input("Cantidad a agregar: "))
                if agregar>0:
                    Modificaciones = Cant_Pro[Posiciones]+agregar
                    Cant_Pro[Posiciones]=Modificaciones
                    print("Agregado con exito")
                    continuar = 1
                elif agregar<=0:
                    agregar=0
                    Modificaciones = Cant_Pro[Posiciones]+agregar
                    Cant_Pro[Posiciones]=Modificaciones
                    print("Agregado sin exito")
                    continuar = 1
    elif Opcion==5:
        Cod_Pro=input("Codigo del producto: ")
        Posiciones = Codigos_Pro.index(Cod_Pro)
        if Cod_Pro==Codigos_Pro[Posiciones]:
                print("")
                print(f'Codigo del producto: {Codigos_Pro[Posiciones]}') 
                print(f'Nombre del producto: {Productos[Posiciones]}') 
                print("Valor Unitario del producto ${:,}".format(costo_unitario[Posiciones]).replace(',','~').replace('.',',').replace('~','.')) 
                print(f'Cantidad: {Cant_Pro[Posiciones]} Unidades')
                print("")
        else:
            print("Incorrecto, intente mas tarde")        
        if Codigos_Pro[Posiciones]==Cod_Pro:
            if Cant_Pro[Posiciones]>=0:
                sacar = int(input("Cantidad a sacar: "))
                if sacar>0 and Cant_Pro[Posiciones]>=sacar:
                    Modificaciones = Cant_Pro[Posiciones]-sacar
                    Cant_Pro[Posiciones]=Modificaciones
                    print("Modificado con exito")
                    continuar = 1
                elif sacar<0 or Cant_Pro[Posiciones]<sacar:
                    sacar=0
                    Modificaciones = Cant_Pro[Posiciones]-sacar
                    Cant_Pro[Posiciones]=Modificaciones
                    print("Modificado sin exito")
                    continuar = 1
    elif Opcion==6:
        print("Adios")
        exit()