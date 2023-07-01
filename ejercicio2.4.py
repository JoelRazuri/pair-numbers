""" 
Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario.
"""

print("---------------------------------------------")
print("NUMEROS PARES ENTRE DOS NUMEROS ")
num_inicio=int(input("Ingrese un numero inicial:"))
num_final=int(input("Ingrese otro numero final:"))
print("")

for par in range(num_inicio,num_final):
    if par%2 == 0:
        print(par,end=" ")