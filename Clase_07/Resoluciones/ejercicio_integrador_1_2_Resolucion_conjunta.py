"""
1. Escribir una función que calcule el máximo común divisor entre dos números. 
2.  Escribir una función que calcule el mínimo común múltiplo entre dos números.
"""
# Para hallar el máximo común divisor utilizo el algoritmo de Euclides. Si uno de los números es cero, entonces el mcd es el otro número.
print('Este programa entrega el máximo común divisor y el mínimo común múltiplo entre dos números')
def mcd_mcm():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    n1 = a              # asigno a n1 el valor ingresado (1er número) porque a va a cambiar de valor en el while
    n2 = b              # asigno a n2 el valor ingresado (2o número) porque b va a cambiar de valor en el while
    if n1 == 0 and n2 != 0:
        print(f"El máximo común divisor entre {n1} y {n2} es {n2}")
    elif n2==0 and n1!=0:
        print(f"El máximo común divisor entre {n1} y {n2} es {n1}")
    else:
        c = a % b       # calcula el resto de la división entre los números ingresados
        while c!= 0:
            d = a % b   # resto de la división de a/b o de b/a (divide al dividendo -número mayor- por el vivisor -número menor-)
            a = b       # el divisor se convierte en dividendo
            b = d       # el resto en divisor
            c = a%b     # vuelve a calcular el resto
        print(f"El máximo común divisor entre {n1} y {n2} es {b}")
       

# Determinación del mínimo común múltiplo como el producto de los dos números dividido el mcd
    
    if n1==0 or n2==0:
        print(f"El mínimo común múltipo entre {n1} y {n2} es 0")
    else:
        mult=int(n1*n2/b)
        print(f"El mínimo común múltipo entre {n1} y {n2} es {mult}")

mcd_mcm()