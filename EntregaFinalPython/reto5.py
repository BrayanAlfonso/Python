'''
RETO 5 ADICIONAL
3 En 2022 el país A tendrá una población de 25 millones de habitantes
y el país B de 18.9 millones. Las tasas de crecimiento anual de la
población serán de 2% y 3% respectivamente. Desarrollar un
programa que imprima el año en que la población del país B superará
a la de A.'''

año=2022
paisA=25000000
paisB=18900000


while paisB<=paisA:
    incrementA=paisA*0.02
    incrementB=paisB*0.03

    año=año+1

    paisA=+paisA+incrementA
    paisB=paisB+incrementB

print("El año en el que la poblacion del pais B supera al de A es el año: "+str(año))