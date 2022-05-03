def holaMundo():
    print("Hola mundo")

def mayorMenorNueve(a):
    if(a>9):
        print(f"El numero ingresado es mayor a 9")
    else:
        print("El numero ingresado no es mayor a 9")

def parImpar(b):
    if(b%2==0): #%algo lo que hace es ofrecer el resto de la division
        print("Es par")
    else:
        print("Es impar")

def sumaNum(c, d):
    print(f"{c+d}") 

def sumaPares():
    contador=2
    sum=0
    while(contador<=100):
        sum+=contador
        contador+=2
    print(sum)

def divisores(e):
    cont=e
    while(cont>0):
        if(e%cont==0):
            print(cont)
        cont-=1

def aprobadoSuspenso(f, g, h):
    res=(f+g+h)/3
    if(res>=5):
        print("Aprobado")
    else:
        print("Suspenso")

def nombreCant(i, j):
    while(j>0):
        print(i)
        j-=1

def sumCincuenta():
    cont=50
    n=0
    while(cont>0):
        n=n+cont
        cont-=1
    print(n)

def numNeg(k, l, m):
    if(k<0):
        print(f"{k*l*m}")
    else:
        print(f"{k+l+m}")

def esPrimo(n):
    if(n%2!=0):
        if(n%1==0 & n%n==0):
            print(f"{n} es primo")
    else:
        print(f"{n} no es primo")

def sumDigits(o):
    p = 0
    for q in str(o): #str = transforma la o en una linea de texto
        p+=int(q) #int = devuelve los valores del str
    print(p,"hola")


holaMundo() #Hola mundo
mayorMenorNueve(5) #Mayor o menor a 9
parImpar(2) #Par o impar
sumaNum(3, 5) #Suma de dos numeros
sumaPares() #Suma de los numeros pares entre 2 y 100
divisores(30) #Divisores de un numero
aprobadoSuspenso(5,5,4) #Media de tres numeros
nombreCant("Jesus", 3) #Escribir un nombre una cantidad de veces
sumCincuenta() #Sumar los primeros 50 numeros naturales
numNeg(2,3,5) #Si el primero es negativo multiplicar los 3 si es positivo sumar los 3
esPrimo(11) #Determinar si un numero es primo
sumDigits(123) #Sumar los digitos de un numero