def numCuadrado():
    print("Ingrese un numero del 1 al 30: ")
    a=input()
    a=int(a)
    print(a*a)
        

def numPrimos():
    b=input("Introduzca un numero: ")
    b=int(b)
    div=2
    band=True
    if(b==1): #poner dos signos de igual para equiparar == !=
        print("Es primo")
    else:
        while(band==True and b>div):
            if(b%div == 0):
                band=False
            div+=1
        if(band==True):
            print("Es primo")
        else:
            print("No es primo")

def avionPapel():
    print("Conseguir hoja de papel.")
    print("Doblarla.")
    print("Darle forma de avión.")

def operaciones():
    c = input("Ingrese un número del 1 al 4: 1 = suma, 2 = resta, 3 = multiplicación, 4 = división.: \n") #la barra n es para que salte linea
    c = int(c)
    if(c==1):
        num1=input("Intrese el valor del primer número (a): ")
        num1=int(num1)
        num2=input("Ingrese el valor del segundo numero (b): ")
        num2=int(num2)
        print(f"{num1+num2}")
    elif(c==2):
        num1=input("Intrese el valor del primer número (a): ")
        num1=int(num1)
        num2=input("Ingrese el valor del segundo numero (b): ")
        num2=int(num2)
        print(f"{num1-num2}")
    elif(c==3):
        num1=input("Intrese el valor del primer número (a): ")
        num1=int(num1)
        num2=input("Ingrese el valor del segundo numero (b): ")
        num2=int(num2)
        print(f"{num1*num2}")
    elif(c==4):
        num1=input("Intrese el valor del primer número (a): ")
        num1=int(num1)
        num2=input("Ingrese el valor del segundo numero (b): ")
        num2=int(num2)
        print(f"{num1//num2}") # poner dos // barras especifica que sea una division de enteros
    
def volArea():
    d=input("Ingrese la altura: ")
    d=int(d)
    e=input("Ingrese el radio: ")
    e=int(e)
    print(f"El volumen es: {3.14*(e*e)*d}")
    print(f"El volumen es: {2*3.14*e*(e*d)}")

def libroBiblio():
    print("Ir a biblioteca")
    print("Pedir libro")
    tenerCarnet=True
    if(tenerCarnet):
        print("Sacar libro")
    else:
        print("Sacar carnet")

def mayorTres():
    f=input("Ingresar el primer numero: ")#pedimos un numero al usuario que se recibe en una variable STR
    g=input("Ingresar el segundo numero: ")
    h=input("Ingresar el tercer numero: ")
    f=int(f)#transformamos la variable STR en una variable INT para poder hacer operaciones aritmeticas con ella
    g=int(g)
    h=int(h)
    if(f>g and f>h):
        print(f"{f} es el mayor numero")
    elif(g>f and g>h):
        print(f"{g} es el mayor numero")
    elif(h>f and h>g):
        print(f"{h} es el mayor numero")

def factorial():
    i=input("Escriba un numero: ")
    i=int(i)
    fact=1
    while(i>=1):
        fact=fact*i
        i-=1
    print(f"Factorial = {fact}")

def mayorMenor():
    j=input("Escriba un numero (a): ")
    k=input("Escrina un numero (b): ")
    if(j>k):
        print(f"El numero mayor es {j} y el menor es {k}")
    elif(k>j):
        print(f"El numero mayor es {k} y el menor es {j}")

def adivinaPalabra():
    print("Ni idea")

numCuadrado() #Cuadrado de un nuemro
numPrimos() #es primo?
avionPapel() #bs
operaciones() #calculadora basica
volArea() #volumen y area
libroBiblio() #bs2:bsing
mayorTres() #mayor de tres numeros
factorial() #sacar factorial
mayorMenor() #saber cual es el menor y el mayor
adivinaPalabra() #bs3:with a vengeance