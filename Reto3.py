import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print("\n"+"Cantidad De Pacientes: ")
cant_pacientes = int(input())

clearConsole()


for i in range(0, cant_pacientes):
    print( "Escoja Un Numero")
    print("Cual es su genero")
    print("1. para Femenino")
    print("2. para Masculino")
    genero = input()
    clearConsole()
    nombre = input("¿Cómo te llamas?:  ")
    clearConsole()
    print("Digite su nivel de hemoglobina actual: ")
    hemoglobina = float(input())
    if genero==1:
        if hemoglobina>13.2:
            print("Alerta N*1")
        else:
            if hemoglobina<16.6:
                print("Alerta N*2")
            else:
                if hemoglobina==13.2 or 16.6:
                    print("Sin Alertas")
    else: 
        if genero==2:
            if hemoglobina>11.6:
                print("Alerta N*1")
            else:
                if hemoglobina<15:
                    print("Alerta N*2")
                else:
                    if hemoglobina==11.6 or 15:
                        print("Sin Alertas")
        else:
             print("El numero seleccionado no se encuentra Vuelva a intentarlo")

print("Nada") 




