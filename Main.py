import Operaciones

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))
op = input("Que operacion desea hacer (suma, resta, multiplicacion, division): ")

if op == "suma":
    resultado = Operaciones.sumar(a, b)
elif op == "resta":
    resultado = Operaciones.restar(a, b)
elif op == "multiplicacion":
    resultado = Operaciones.multiplicar(a, b)
elif op == "division":
    resultado = Operaciones.dividir(a, b)
else:
    resultado = 0
    print("Operacion no reconocida")

if resultado != 0:
    print(f"Resultado: {resultado}")
