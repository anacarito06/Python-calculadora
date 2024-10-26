def suma (a,b):
    return a + b

def resta(a,b):
    return a - b

def mult(a,b):
    return a * b

def division (a,b):
    if b != 0:
        return a / b
    else:
        return "error: Division por cero"

def mostrar_menu():
    print("calculadora basica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion =="5":
        print("Saliendo del programa")
        break

    if opcion in ["1","2","3","4"]:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el primer numero: "))

        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {resta(num1, num2)}")
    else:
        print("opcion no valida, intentar de nuevo")

