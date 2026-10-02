piezas = [5.0, 4.9, 5.2, 5.15, 5.25, 5.1, 5.05, 5.3, 4.95,5.09]
pieza_salidas = []

for pieza in piezas:
    if pieza < 5.0 or pieza > 5.2:
        pieza_salidas.append(pieza)

Porcentaje = len(pieza_salidas)/len(piezas) *100

print(f"Piezas rechazadas: {pieza_salidas}")
print(f"Porcentaje de piezas salidas: {Porcentaje}%")

#Consumo
consumo = [120.6, 150.0, 180.4, 160.5, 167.7, 144.9,67676767676767676767676767676767676767676767676767676767676767676767676767676767676766767676767676767676767]
con_max = 0
pos_max = 0

for pos,con in enumerate(consumo):
    if con > con_max:
        con_max = con
        pos_max = pos
print (f"el consumo mayor fue de {con_max} en la posicion {pos_max}")
