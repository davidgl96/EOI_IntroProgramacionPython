ciudad="madrid"
print(ciudad.isdigit())
minombre="david"
print(len(minombre))

print(minombre[0])
print(minombre[1])
print(minombre[4])

mensaje = "dd"
ciudad = "albacete"
print("hola {m} de {c}" .format(m=mensaje,c=ciudad)) #eficiente
print("hola "+mensaje) #no eficiente

numero = 10/3
print("El numero sin formato es: {}".format(numero))

print("El numero con formato es: {n:1.2f}".format(n=numero)) #1.2f es para que de dos decimales

print(f"Hola {mensaje} de {ciudad}") #f = concatenar
