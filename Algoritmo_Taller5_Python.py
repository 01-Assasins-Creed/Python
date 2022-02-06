seguir = 1
while seguir == 1:
    print();
    print("Taller N5 de algoritmo");
    print();

    print("Opcion 1. Calcular el promedio de 5 asignaturas de un N_Estudiantes");
    print("Opcion 2. Procesar N_Cantidad de clientes con television por cable");
    print("Opcion 3. Calcular el promedio de Bateos de N_Jugadores");

    Opcion=int(input("Selecione la opcion del algoritmo a utilizar: ")) 

    if Opcion==1:
        Cant_Estudent = int(input("Escriba la cantidad de estudiantes a buscar promedio: "))
        retirados = 0
        P_prueba = 0
        P_normal = 0
        P_Dist = 0
        for a in range(Cant_Estudent):
            prom_Estudent=0
            nombre = input(f'Estudiante #{a+1} Escriba Su Nombre: ')
            for b in range(5):
                nota_asig = float(input(f'Escriba la definitiva de la asignatura #{b+1}: '))
                prom_Estudent = prom_Estudent + nota_asig
            prom_Estudent = prom_Estudent/5
            print();
            print(f'Estudiante: {nombre}')
            print(f'El total de su promedio Es: {prom_Estudent}')
            if prom_Estudent < 3:
                print(f'Estudiante: {nombre}', 'Retirado del programa')
                retirados = retirados + 1; 
            elif prom_Estudent >= 3 and prom_Estudent < 3.5:
                print(f'Estudiante: {nombre}', 'Esta en periodo de prueba')
                P_prueba = P_prueba + 1
            elif prom_Estudent >= 3.5 and prom_Estudent < 4.5:
                print(f'Estudiante: {nombre}', 'Esta en estado normal')
                P_normal = P_normal + 1
            elif prom_Estudent >= 4.5:
                print(f'Estudiante: {nombre}', 'Esta dentro de los estudiante distinguido')
                P_Dist = P_Dist + 1
            print();    
        print();        
        print(f'Estudiantes retirados: {retirados}')
        print(f'Estudiantes en periodo de prueba: {P_prueba}')
        print(f'Estudiantes en estado normal: {P_normal}')
        print(f'Estudiantes distinguidos: {P_Dist}')
        print();
        print("Opcion 1. Volver al menu de inicio");
        print("Opcion 2. Salir");
        seguir = input('Seleccione una opcion: ')
    elif Opcion==2:
        cant_Clientes = int(input("Escriba el total de clientes analizar: "))
        for a in range(cant_Clientes):
            codigo = input(f'Cual es el codigo del Cliente #{a+1}: ')
            print("Opcion: 1. Residencial")
            print("Opcion: 2. Empresarial")
            tp_client = int(input("Que tipo de cliente es: "))
            Lect_Act = int(input("Cual fue la lectura actual del Cliente: "))
            Lect_Ant = input("Cual fue la lectura anterior del Cliente: ")
            fijo=20000
            
            if tp_client == 1:
                valor_sin_iva = 100*Lect_Act
                iva = (100*Lect_Act)*0.19
                valor_Con_iva = (100*Lect_Act)+iva
                Total_Pagar = valor_Con_iva+fijo
            elif tp_client == 2:
                valor_sin_iva = 150*Lect_Act
                iva = (150*Lect_Act)*0.19
                valor_Con_iva = (150*Lect_Act)+iva
                Total_Pagar = valor_Con_iva+fijo
                print();        
            print(f'Codigo: {codigo}')
            print(f'Usted gasto {Lect_Act} impulsos')
            print(f'Costo sin iva Es: {valor_sin_iva}')
            print(f'El costo total Es: sin iva: {valor_sin_iva} + iva: {iva} + fijo {fijo} = {Total_Pagar}')
            print()
        print();
        print("Opcion 1. Volver al menu de inicio");
        print("Opcion 2. Salir");
        seguir = input('Seleccione una opcion: ')
    elif Opcion ==3:
        cant_Jugadores = int(input("Escriba la cantidad dee Jugadores a calcular el promedio de bateo: "))
        for a in range(cant_Jugadores):
            nombre = input(f'Jugador #{a+1} Cual es Su Nombre: ')
            VB = int(input("Cantidad de veces que ha bateado: "))
            HIT = int(input("Cantidad de Hit Conectados: "))
            EXT = int(input("Cantidad de Extrabases Conectados: "))
            S = int(input("Cantidad de Sacrificios: "))
            BB = int(input("Cantidad de Bases por Bolas Recibidas: "))
            BBC = HIT + EXT
            VLB = VB-S-BB
            PB = BBC / VLB * 1000
            print();        
            print(f'Jugador: {nombre}')
            print(f'El promedio de su bateo es de: {PB}')
            print();
        print();    
        print("Opcion 1. Volver al menu de inicio")
        print("Opcion 2. Salir")
        seguir = input('Seleccione una opcion: ')
    else:
        print("Error, Vuelva a intentar")
        print();
        print("Opcion 1. Volver al menu de inicio")
        print("Opcion 2. Salir")
        seguir = input('Seleccione una opcion: ')
print("Acabas de salir")