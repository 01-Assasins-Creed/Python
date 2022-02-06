import numpy as np

#Constantes de valores
dos_salarios=1817052
Num_Empleados = 5
i=0

#Deducciones
Salud=0.04
Pension = 0.04
Arl = 0.01


#Almacenar los pagos finales para ordenar
Vector_Total=[]
#Evitar cedulas iguales
Num_Ident=[]
#Recolector de nombres
Lista_Nombres = []
#Vector_Total sin modificar
Vector2_Total=[]

rep=0
longitud =0
for i in range (Num_Empleados): 
    intentos=1
    aux_tran=106454
    print("")
    resp=True
    seguir=True
    while resp or seguir:
        try:
            Identificacion = int(input(f'Trabajador #{i+1}, Digite su número de identificación: '))
            resp=False
            seguir=False
            if longitud==0:
                Num_Ident.append(Identificacion)
                longitud = len(Num_Ident)
            else:
                for rep in range(longitud):
                    if Num_Ident[rep]==Identificacion:
                        print("El número de identificación ya se encuentra registrado")
                        seguir = True
                    elif Num_Ident[rep]!=Identificacion:
                        Num_Ident.append(Identificacion)
                        longitud = len(Num_Ident)
        except ValueError:
            print("Solamente se permiten números enteros positivos") 
    while Identificacion<0 or Identificacion<9999999:
        resp2=True
        seguir=True
        while resp2 or seguir:
            try:
                print(f'Trabajador #{i+1}, Su número de identificación debe tener 8 digitos como mínimo y además estos deben ser positivos')
                Identificacion = int(input(f'Trabajador #{i+1}, Digite su número de identificación: (Intento: #{intentos+1}) : '))
                intentos=intentos+1
                resp2=False
                seguir=False
                if longitud==0:
                    Num_Ident.append(Identificacion)
                    longitud = len(Num_Ident)
                else:
                    for rep in range(longitud):
                        if Num_Ident[rep]==Identificacion:
                            print("El número de identificación ya se encuentra registrado")
                            seguir = True
                        elif Num_Ident[rep]!=Identificacion:
                            Num_Ident.append(Identificacion)
                            longitud = len(Num_Ident)
            except ValueError:
                print("Solamente se permiten número enteros positivos")
        if intentos>3 and resp2==False:
            print("")
            print(f'Trabajador #{i+1}, se alcanzó el límite permitido, intente nuevamente')
            print("")
            exit()
            
    Nombre = input(f'Trabajador #{i+1}, Digite su nombre completo: ')
    Lista_Nombres.append(Nombre)
    
    print("")
    print("Marque 1 si gana un salario mínimo legal vigente (SMLV) ")
    print("Marque 2 si gana más de un salaerio mínimo legal vigente (SMLV)")
    print("Nota: Un salario mínimo legal vigente (SMLV) actualmente corresponde a $908526")
    opcion= int(input(f'Trabajador #{i+1}, Digite una opcion: '))
    print("")
    print("")
    if opcion==1:
        Horas_E_D=0
        Salario = 908526
        entrada=True
        while entrada or Horas_E_D<0 or Horas_E_D>24:
            try:
                Horas_E_D= int(input(f'Trabajador #{i+1}, digite la cantidad de horas extras diurnas que laboró: '))
                if Horas_E_D>24:
                    print("No se pueden ingresar más de 24 horas extras.")
                elif Horas_E_D<0:
                    print("No se pueden ingresar menos de 0 horas extras.")
                entrada=False
            except ValueError:
                print("Solamente se permiten números enteros positivos") 
        
        if Horas_E_D==0:
            Valor_E_D=0
        elif Horas_E_D>0:
            Valor_E_D=Salario/240
            result = Valor_E_D*0.25
            Valor_E_D=Valor_E_D+result
            Valor_E_D=round(Valor_E_D)
            print("Valor por horas extras es:  $ {:,}".format(Valor_E_D).replace(',','~').replace('.',',').replace('~','.'))
        if Salario<=dos_salarios and Horas_E_D<=10:
            #Se multiplica el total de horas trabajadas por el valor de la hora
            Total_E_D = Horas_E_D*Valor_E_D
            #se calcula los devengos en base a si recibe o no auxilio de transporte
            Devengos = Salario+aux_tran+Total_E_D
            print("Su auxilio de transporte es de:  $ {:,}".format(aux_tran).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Salud = 0.04 nos da como resultado 48.000
            Ded_Salud = Devengos*Salud
            Ded_Salud = round(Ded_Salud)
            print("La deducción por Salud es:  $ {:,}".format(Ded_Salud).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Pension = 0.04 nos da como resultado 48.000
            Ded_Pension = Devengos*Pension
            Ded_Pension = round(Ded_Pension)
            print("La deducción por Pensión es:  $ {:,}".format(Ded_Pension).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante ARL = 0.01 nos da como resultado 12.000
            Ded_ARL = Devengos*Arl
            Ded_ARL = round(Ded_ARL)
            print("La deducción por ARL es:  $ {:,}".format(Ded_ARL).replace(',','~').replace('.',',').replace('~','.')) 
            #Todo lo anterior se le va a restar al Devengo y se guardara en el total a pagar es decir: Total_Pagar=1.200.000-48.000-48.000-12.000 Nos arroja el total = 1.092.000
            Total_Pagar = Devengos-Ded_Salud-Ded_Pension-Ded_ARL
            Vector_Total.append(Total_Pagar)
            Vector2_Total.append(Total_Pagar)
        else:
            aux_tran=0
            print("Su auxilio de transporte es de:  $ {:,}".format(aux_tran).replace(',','~').replace('.',',').replace('~','.')) 
            #Se multiplica el total de horas trabajadas por el valor de la hora
            Total_E_D = Horas_E_D*Valor_E_D
            #se calcula los devengos en base a si recibe o no auxilio de transporte
            Devengos = Salario+Total_E_D
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Salud = 0.04 nos da como resultado 48.000
            Ded_Salud = Devengos*Salud
            Ded_Salud = round(Ded_Salud)
            print("La deducción por Salud es:  $ {:,}".format(Ded_Salud).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Pension = 0.04 nos da como resultado 48.000
            Ded_Pension = Devengos*Pension
            Ded_Pension = round(Ded_Pension)
            print("La deducción por Pensión es:  $ {:,}".format(Ded_Pension).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante ARL = 0.01 nos da como resultado 12.000
            Ded_ARL = Devengos*Arl
            Ded_ARL = round(Ded_ARL)
            print("La deducción por ARL es:  $ {:,}".format(Ded_ARL).replace(',','~').replace('.',',').replace('~','.')) 
            #Todo lo anterior se le va a restar al Devengo y se guardara en el total a pagar es decir: Total_Pagar=1.200.000-48.000-48.000-12.000 Nos arroja el total = 1.092.000
            Total_Pagar = Devengos-Ded_Salud-Ded_Pension-Ded_ARL
            Vector_Total.append(Total_Pagar)
            Vector2_Total.append(Total_Pagar)
    elif opcion==2:
        resp=True
        Salario=0
        while resp or Salario<0 or Salario>4542630:
            try:
                Salario = int(input(f'Trabajador #{i+1}, digite su salario básico: '))
                if Salario<0:
                    print("No se pueden ingresar valores negativos.")
                elif Salario>4542630:
                    print("El valor máximo del salario básico es de cinco salarios mínimos legales vigentes (SMLV), es decir, $4.542.630")
                resp=False
            except ValueError:
                print("Solamente se permiten números") 
        entrada=True
        while entrada or Horas_E_D<0 or Horas_E_D>24:
            try:
                Horas_E_D= int(input(f'Trabajador #{i+1}, digite la cantidad de horas extras diurnas que laboró: '))
                if Horas_E_D>24:
                    print("No se pueden ingresar más de 24 horas extras.")
                elif Horas_E_D<0:
                    print("No se pueden ingresar menos de 0 horas extras.")
                entrada=False
            except ValueError:
                print("Solamente se permiten número enteros positivos") 
        if Horas_E_D==0:
            Valor_E_D=0
        elif Horas_E_D>0:
            Valor_E_D=Salario/240
            result = Valor_E_D*0.25
            Valor_E_D=Valor_E_D+result
            Valor_E_D=round(Valor_E_D)
            print("Valor por horas extras es:  $ {:,}".format(Valor_E_D).replace(',','~').replace('.',',').replace('~','.')) 
        if Salario<=dos_salarios and Horas_E_D<=10:
            #Se multiplica el total de horas trabajadas por el valor de la hora
            Total_E_D = Horas_E_D*Valor_E_D
            #se calcula los devengos en base a si recibe o no auxilio de transporte
            Devengos = Salario+aux_tran+Total_E_D
            print("Su auxilio de transporte es de:  $ {:,}".format(aux_tran).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Salud = 0.04 nos da como resultado 48.000
            Ded_Salud = Devengos*Salud
            Ded_Salud = round(Ded_Salud)
            print("La deducción por Salud es:  $ {:,}".format(Ded_Salud).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Pension = 0.04 nos da como resultado 48.000
            Ded_Pension = Devengos*Pension
            Ded_Pension = round(Ded_Pension)
            print("La deducción por Pensión es:  $ {:,}".format(Ded_Pension).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante ARL = 0.01 nos da como resultado 12.000
            Ded_ARL = Devengos*Arl
            Ded_ARL = round(Ded_ARL)
            print("La deducción por ARL es:  $ {:,}".format(Ded_ARL).replace(',','~').replace('.',',').replace('~','.')) 
            #Todo lo anterior se le va a restar al Devengo y se guardara en el total a pagar es decir: Total_Pagar=1.200.000-48.000-48.000-12.000 Nos arroja el total = 1.092.000
            Total_Pagar = Devengos-Ded_Salud-Ded_Pension-Ded_ARL
            Vector_Total.append(Total_Pagar)
            Vector2_Total.append(Total_Pagar)
        else:
            aux_tran=0
            #Se multiplica el total de horas trabajadas por el valor de la hora
            Total_E_D = Horas_E_D*Valor_E_D
            #se calcula los devengos en base a si recibe o no auxilio de transporte
            Devengos = Salario+Total_E_D
            print("Su auxilio de transporte es de:  $ {:,}".format(aux_tran).replace(',','~').replace('.',',').replace('~','.')) 
           #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Salud = 0.04 nos da como resultado 48.000
            Ded_Salud = Devengos*Salud
            Ded_Salud = round(Ded_Salud)
            print("La deducción por Salud es:  $ {:,}".format(Ded_Salud).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante Pension = 0.04 nos da como resultado 48.000
            Ded_Pension = Devengos*Pension
            Ded_Pension = round(Ded_Pension)
            print("La deducción por Pensión es:  $ {:,}".format(Ded_Pension).replace(',','~').replace('.',',').replace('~','.')) 
            #Se calculan cuando te va a deducir del devengo es decir: Devengos=1.200.000 por la constante ARL = 0.01 nos da como resultado 12.000
            Ded_ARL = Devengos*Arl
            Ded_ARL = round(Ded_ARL)
            print("La deducción por ARL es:  $ {:,}".format(Ded_ARL).replace(',','~').replace('.',',').replace('~','.')) 
            #Todo lo anterior se le va a restar al Devengo y se guardara en el total a pagar es decir: Total_Pagar=1.200.000-48.000-48.000-12.000 Nos arroja el total = 1.092.000
            Total_Pagar = Devengos-Ded_Salud-Ded_Pension-Ded_ARL
            Vector_Total.append(Total_Pagar)
            Vector2_Total.append(Total_Pagar)
            
print("")
print("")            
print("Toda la informacion ha sido recolectada correctamente")
print("")
print("¿Cómo desea mostrar los resultados?")
print("")
print("Marque 1 para ordenar de forma ascendente")
print("Marque 2 para ordenar de forma descendente")
print("Marque 3 para ordenar de ambas formas")
Mostrar= int(input("Digite una opción: "))
print("")
if Mostrar==1:
    print("")
    print("Los totales a pagar a los empleados de forma ascendente son:")
    Vector_Total.sort()
    for a in range(5):
        z=0
        a1=0
        while a1<5:
            if Vector2_Total[z]==Vector_Total[a]:
                print(f'Trabajador {Lista_Nombres[z]} '+" Su pago es: $ {:,}".format(Vector_Total[a]).replace(',','~').replace('.',',').replace('~','.')) 
            z=z+1
            a1=a1+1
elif Mostrar==2:
    print("")
    print("los totales a pagar a los empleados de forma descendente son:")
    Vector_Total.sort(reverse=True)
    for d in range(5):
        z=0
        a1=0
        while a1<5:
            if Vector2_Total[z]==Vector_Total[d]:
                print(f'Trabajador {Lista_Nombres[z]} '+" Su pago es: $ {:,}".format(Vector_Total[d]).replace(',','~').replace('.',',').replace('~','.')) 
            z=z+1
            a1=a1+1 
    print("")
elif Mostrar==3:
    print("")
    print("los totales a pagar a los empleados de forma ascendente son:")
    Vector_Total.sort()
    for a in range(5):
        z=0
        a1=0
        while a1<5:
            if Vector2_Total[z]==Vector_Total[a]:
                print(f'Trabajador {Lista_Nombres[z]} '+" Su pago es: $ {:,}".format(Vector_Total[a]).replace(',','~').replace('.',',').replace('~','.')) 
            z=z+1
            a1=a1+1 
    print("")
    print("los totales a pagar a los empleados de forma descendente son:")
    Vector_Total.sort(reverse=True)
    for d in range(5):
        z=0
        a1=0
        while a1<5:
            if Vector2_Total[z]==Vector_Total[d]:
                print(f'Trabajador {Lista_Nombres[z]} '+" Su pago es: $ {:,}".format(Vector_Total[d]).replace(',','~').replace('.',',').replace('~','.')) 
            z=z+1
            a1=a1+1 




