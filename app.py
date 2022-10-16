from random import randint
from functools import reduce

numeros = [numero for numero in range(1,randint(10,100))]
print('\nlista de números:\n',numeros)
impares = list(filter(lambda num: num%2 == 0,numeros))
print('\nimpares de la lista:\n',impares)
suma = reduce(lambda num1,num2: num1+num2 ,impares)
print('\nLa suma de todos los impares es:',suma)