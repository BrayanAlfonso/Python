'''
RETO 1
Diseñe una función que calcule la cantidad de carne de aves en kilos
si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6
kilos, 7 kilos y 1 kilo respectivamente.
'''

def calcular(gallinas,gallos,pollitos):
    cantGallinas=gallinas*6
    cantGallos=gallos*7
    cantPollitos=pollitos*1

    print("La cantidad en kilogramos de carne de gallinas es: "+str(cantGallinas))
    print("La cantidad en kilogramos de carne de gallos es: "+str(cantGallos))
    print("La cantidad en kilogramos de carne de pollitos es: "+str(cantPollitos))



calcular(5,7,10)