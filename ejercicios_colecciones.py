import json
from random import randint
#Ejercicios de colecciones 

# 1. Hacer un programa que procese 100 mujeres y hombres (M/H). 
# Mostrar el porcentaje de hombres y mujeres y si hay más 
# mujeres que hombres, si hay igualdad o si hay más hombres 
# que mujeres.
#def randCien():
#    n = randint(1,100)
#    return(n)
#
#def mujeresHombres():
#    mujeres=randCien()
#    hombres=randCien()
#    if(mujeres==hombres):
#        print("Misma cantidad de mujerse y hombres.")
#    elif(mujeres>hombres):
#        print("Hay mas mujeres que hombres.")
#    elif(hombres>mujeres):
#        print("Hay mas hombres que mujeres.")

#mujeresHombres()

# 2. Hacer un programa que procese las edades de 100 personas. 
# Deberá decir cuantas tienen más de (≥18) y cuál es la persona
# con menor edad y cuál es la persona con mayor edad. También 
# deberá mostrar el porcentaje de edades de las 100 personas.
 
#ef generarPersonas():
#   num = 0
#   personas = [0]*100
#   prom=0
#   mayorEdadCont = 0
#   mayorEdad = 0
#   menorEdad =0
#   while num < 100:
#       personas[num] = randCien()
#       num+=1
#   for   persona in personas:
#       prom = prom+persona
#       if persona>=18:
#           mayorEdadCont+=1
#       if menorEdad>=persona:
#           menorEdad=persona
#       elif mayorEdad<=persona:
#           mayorEdad=persona
#   print(f"La persona con menor edad tiene: {menorEdad} años")
#   print(f"La persona con mayor edad tiene: {mayorEdad} años")
#   print(f"El promedio de edad es {prom/100}")
#   print(f"Hay {mayorEdadCont} personas de mas de 18 años")

#generarPersonas()
  
# 3. Hacer un programa que procese un total de 100 personas y 
# establecer cuantas son mujeres mayores de edad y cuantos 
# hombres menores de edad. Deberá sacar el hombre y la mujer 
# con menor edad, el hombre y la mujer con mayor edad, 
# promedio de edades de las mujeres y promedio de edades de 
# los hombres.

#ejercicio 1
class Alguien:
    def __init__(self, age, genre):
        self.age=age
        self.genre=genre

def ejercicios123():
    a=0
    personas=[object]*100
    contHombre=0
    contMujer=0
    mayEighteen=0
    maxEdad=0
    minEdad=0
    cantMujMayEdad=0
    cantHomMenEdad=0
    mujMayEdad=0
    homMayEdad=0
    mujMenEdad=0
    homMenEdad=0
    promMuj=0
    promHom=0

    while a<100:

        edad=randint(0,100)
        genero=randint(0,1)
        personas[a]=Alguien(edad, genero)

        #Set de comprobaciones
        if personas[a].genre==1:
            contHombre+=1
            promHom+=personas[a].age

            if homMayEdad<personas[a].age:
                homMayEdad=personas[a].age

            if homMenEdad>personas[a].age:
                homMenEdad=personas[a].age 

        if personas[a].genre==0:
            contMujer+=1
            promMuj+=personas[a].age

            if mujMayEdad<personas[a].age:
                mujMayEdad=personas[a].age

            if mujMenEdad>personas[a].age:
                mujMenEdad=personas[a].age  

        if personas[a].age>18:
            mayEighteen+=1

        if minEdad>personas[a].age:
            minEdad=personas[a].age

        if maxEdad<personas[a].age:
            maxEdad=personas[a].age

        if personas[a].genre==0 and personas[a].age>18:
            cantMujMayEdad+=1

        if personas[a].genre==1 and personas[a].age<18:
            cantHomMenEdad+=1

        a+=1
        
    #Resultados
    if contHombre>contMujer:
        print("Hay mas hombres que mujeres")
    
    if contMujer>contHombre:
        print("Hay mas mujeres que hombres")  
    
    if contMujer==contHombre:
        print("Hay el mismo numero de hombres que de mujeres") 

    print(f"Hay {contHombre} hombres")
    print(f"Hay {contMujer} mujeres")
    print(f"Hay {mayEighteen} personas con mas de 18 años")
    print(f"La persona con mayor edad tiene {maxEdad}")
    print(f"La persona con menor edad tiene {minEdad}")
    print(f"Hay {cantMujMayEdad} mujeres mayores de edad")
    print(f"Hay {cantHomMenEdad} hombres menores de edad")
    print(f"El promedio de la edad de los hombres es {promHom//contHombre}")
    print(f"El promedio de la edad de las mujeres es {promMuj//contMujer}")
    print(f"El hombre de mayor edad tiene {homMayEdad} y el de menor edad tiene {homMenEdad}")
    print(f"La mujer de mayor edad tiene {mujMayEdad} y la de menor edad tiene {mujMenEdad}")

ejercicios123()

# 4. Hacer un programa que procese las temperaturas mensuales 
# de 20 ciudades. Deberá sacar cuál de las ciudades tiene en 
# promedio anual la temperatura más alta y cual la más baja. 
# También deberá sacar la lista de las 20 ciudades con el 
# promedio de temperaturas anuales desde la más alta hasta 
# la más baja.

def randTemp():
    return randint(1,31)


tempAlta=0
tempBaja=110
promTemps=0
ite=0
listProms=list()

while ite<=19:
    ciudadTemps = (randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),randTemp(),)
    
    for temperatura in ciudadTemps:
        
        if tempAlta<temperatura:
            tempAlta=temperatura
        
        if tempBaja>temperatura:
            tempBaja=temperatura

        promTemps+=temperatura
        promedio=promTemps//12

    print(f"La temperatura mas alta de la ciudad numero {ite+1} es {tempAlta}")
    print(f"La temperatura mas baja es {tempBaja}")
    print(f"El promedio de las temperaturas es: {promedio}")
    
    listProms.append(promedio)
    promTemps=0
    ite+=1

ite2=1

listProms.sort(reverse=True)
for tempPromedio in listProms:
    print(f"La temperatura promedio de la ciudad {ite2} es {tempPromedio}")
    ite2+=1