'''Dado un número real x, construya una función que permita
determinar si el número es positivo, negativo o cero. Para cada caso
de debe imprimir el texto que se especifica a continuación:
Positivo: “El número x es positivo”
Negativo: “El número x es negativo”
Cero (0): “El número x es el neutro para la suma”'''

def numero(x):
    if x==0:
        print("El numero "+str(x)+" es el neutro para la suma")
    elif x<0:
        print("El numero "+str(x)+" es negativo")
    elif x>0:
        print("El numero "+str(x)+" es positivo")

numero(3.5)