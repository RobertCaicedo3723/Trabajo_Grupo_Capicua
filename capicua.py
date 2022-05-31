
print("----------------------------------------------------------------------")
print("---------Programa para determinar si un número es capicúa-------------")
print("----------------------------------------------------------------------")
print()

# input

X = int(input("Ingrese un número: "))

# Procesing

if X > 99 and X < 1000:
    Y = X // 100
    Z = X % 10
    if Y == Z:
        print("El número " + str(X) + (" es un número capicúa"))
    else:
        print("El número " + str(X) + (" no es un número capicúa"))
else:
    print("Ingrese un número de TRES digitos")