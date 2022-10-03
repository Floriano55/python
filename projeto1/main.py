from asyncio.windows_events import NULL
from token import NEWLINE

print("Projeto 1 - operações matemáticas")

input1 = input("Primeiro valor: ")
input2 = input("Segundo valor: ")

valor1 = int(input1)
valor2 = int(input2)

def sum(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y 

def divide(x,y):
    if (y == 0) :
        print("divisor can´t be zero")
        return NULL
    else :
        return x / y
    
def power(x,y):
    return x ** y
    
    
print("A soma de " + input1 + " e " + input2 + " é igual a " + str(sum(valor1,valor2)))
NEWLINE
print("A diferença de " + input1 + " e " + input2 + " é igual a " + str(subtract(valor1,valor2)))
NEWLINE
print("A multiplicação de " + input1 + " e " + input2 + " é igual a " + str(multiply(valor1,valor2)))
NEWLINE
print("A divisão de " + input1 + " e " + input2 + " é igual a " + str(divide(valor1,valor2)))
NEWLINE
print("A potência de " + input1 + " elevado a " + input2 + " é igual a " + str(power(valor1,valor2)))
NEWLINE