'''
RETO 4
Desarrollar un programa que dado un nÚmero entero positivo n
calcule e imprima (separados por espacios) n/2 si es par o 3n + 1 si es
impar. El programa debe repetir el proceso con el nÚmero resultado
de dicha operación mientras este sea diferente de 1. Por ejemplo para
el nÚmero 3 debe imprimir 10 5 16 8 4 2 1.
'''


numero=int(input("Ingrese un numero"))

while numero!=1:
    if numero%2==0:
        resultado=numero/2
    else:
        resultado=(3*numero)+1
    print(int(resultado), end=" ")
    numero=resultado
