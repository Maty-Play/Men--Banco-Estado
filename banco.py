import os, time
os.system ("cls")

acceso = True
while acceso:
    print("========= BANCO FINANCIERO =========")
    print("1. Mostrar cuotas de ahorro")
    print("2. Simular depósito acumulado")
    print("3. Tabla de crédito")
    print("4. Contar clientes atendidos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            
            monto_ahorro = 0
            mes = 0
            print("1. Mostrar cuotas de ahorro")
            while monto_ahorro <= 0:
                monto_ahorro = int(input("Ingrese monto para ahorro: "))
                if monto_ahorro <= 0:
                    print("El monto debe ser mayor a 0")
            while mes <= 0:
                mes = int(input("Ingrese cantidad de meses para ahorro: "))
                if mes <= 0:
                    print("El mes debe ser mayor a 0")
            
            for i in range(1,mes + 1):
                ahorro_mensual = monto_ahorro * i
                print(f"Mes {i}: ${ahorro_mensual}")
            time.sleep(3)
            
        elif opcion == 2:
            
            deposito = 0
            acumulador_dep = 0
            cantidad_dep = 0
            print("2. Simular depósito acumulado")
            while deposito >= 0:
                deposito = int(input("Ingrese el deposito: "))
                acumulador_dep = acumulador_dep + deposito
                if deposito <= 0:
                    break
                else:
                    cantidad_dep = cantidad_dep + 1
            
            print(f"Total Acumulado: {acumulador_dep}")
            print(f"Cantidad Depositada: {cantidad_dep}")
            
        elif opcion == 3:
            print("3. Tabla de crédito")
            credito = int(input("Ingrese el monto de credito: "))
            for i in range(1,13):
                print(f"{credito} x {i}: ${credito*i}")
        elif opcion == 4:
            print("4. Contar clientes atendidos")
        elif opcion == 5:
            print("5. Salir")
            acceso = False
        else:
            print("Opcion Invalida")
    except:
        print("El valor ingresado debe ser numerico")





