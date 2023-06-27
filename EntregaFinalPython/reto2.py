'''
RETO 2
 Mi mamá me manda a comprar P panes a $ 300 cada uno, M bolsas
de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
programa que me diga las vueltas (o lo que quedo debiendo) cuando
me da un billete de B pesos.'''


panes=int(input("Ingrese la cantidad de panes que vas a comprar: "))
leche=int(input("Ingrese la cantidad de leche que vas a comprar: "))
huevos=int(input("Ingrese la cantidad de huevos que vas a comprar: "))
dinero=int(input("Ingresa el billete con el que vas a pagar: "))


totalPanes=panes*300
totalLeche=leche*3300
totalHuevos=huevos*350
totalDinero=totalPanes+totalLeche+totalHuevos

vueltas=totalDinero-dinero

if vueltas==0:
    print("No te ha sobrado nada!")
elif vueltas<0:
    vueltas_abs = abs(vueltas)
    print("Te ha sobrado "+str(vueltas_abs))
elif vueltas>0:
    print("Has quedado debiendo "+str(vueltas))