suma = 0
print("\tBienvenido!")
print("1. Agua = $600")
print("2. Azúcar = $1.200")
print("3. Aceite = $1.500")
print("4. Arroz = $1.250")
print("5. Fideos = $790")
print("6. Bebida = $.1780")
print("7. Chocolate = $2.500")
print("8. Pan de Molde = $1.340")
cant = int(input("Cuantos productos deseas llevar? "))
for i in range(1, cant+1):
    ped = input("Que item deseas agregar al carrito? ")
    if ped == '1':
        suma = suma + 600
    elif ped == '2':
        suma = suma + 1200
    elif ped == '3':
        suma = suma + 1500
    elif ped == '4':
        suma = suma + 1250
    elif ped == '5':
        suma = suma + 790
    elif ped == '6':
        suma = suma + 1780
    elif ped == '7':
        suma = suma + 2500
    elif ped == '8':
        suma = suma + 1340
print("El monto total a pagar es de",suma)
pref = input("Eres cliente preferencial? ")
if pref == 'si':
    total = suma * 0.75
    print("El monto total a pagar es de",total)
    ing = int(input("Ingrese monto pagado: "))
    if ing < total:
        print("Guardias, vengan rapido!")
    vuelto = ing - total
    print("Tu vuelto es de:",vuelto,"pesos.")
if pref == 'no':
    ing = int(input("Ingrese monto pagado: "))
    if ing < suma:
        print("Guardias, vengan rapido!")
    vuelto = ing - suma
    print("Tu vuelto es de:",vuelto,"pesos.")