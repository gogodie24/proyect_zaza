

saldo = 1000000 

def mostrar_menu():
    print("Bienvenido a Banco Falaferia")
    print("Seleccione una opcion: ")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Cambiar PIN")
    print("4. Retirar dinero")
    print("5. Salir")

def consultar_saldo():
    print(f"Tu saldo actual es: ${saldo:.2f}")

def depositar():
    global saldo
    cantidad = float(input("¿Cuánto deseas depositar? $"))
    if cantidad > 0:
        saldo += cantidad
        print(f"Has depositado ${cantidad:.2f}. Nuevo saldo: ${saldo:.2f}")
    else:
        print("Cantidad inválida.")

def retirar():
    global saldo
    cantidad = float(input("¿Cuánto deseas girar? $"))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
        print(f"Has girado ${cantidad:.2f}. Nuevo saldo: ${saldo:.2f}")
    else:
        print("Saldo insuficiente o cantidad inválida.")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        retirar()
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
