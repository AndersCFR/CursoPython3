# Variables en Python
import math

# 0. None
variableA = None
print(variableA)

variableA = 'Anderson'
print(type(variableA))
print(variableA)

variableA = 52.2
print(type(variableA))
print(variableA)

# 1. Int
entero1 = 15
entero2 = 35
suma = entero1 + entero2
print('Suma', suma)
resta = entero1 - entero2
print('Resta', resta)
multiplicacion = entero1 * entero2
print('Multiplicación', multiplicacion)
division = entero1 / entero2
print('División', division)
divisionEntera = entero1 // entero2
print('Division entera', divisionEntera)
potencia = entero1 ** 4
print('Potencia', potencia)
raiz = entero1 ** (1/5)
print('Raiz 5 de 15: ', raiz)
print('Raiz de 15: ', math.sqrt(15))

# 2. Float
# las mismas operaciones de los ints
float1 = 56.68
float2 = 4.2
print('División', float1/float2)
print('Otro flotante', float(entero2))

# Castings
estatura = float(input('Estatura: '))
print('Estatura', estatura/2)