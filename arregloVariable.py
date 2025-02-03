sArray = int(input ("Ingrese el tamaño del arreglo: "))
lista = []
for i in range(sArray):
    valor = int(input (f"Ingrese el valor para la posición {i} del Arreglo :"))
    lista.append(valor)

import pandas as pd
df = pd.DataFrame(lista)
print ("El promedio de los datos ingresados es: " df[0].mean())
print ("El valor máximo entre los datos ingresados es: " df[0].max())
print ("El valor mínimo entre los datos ingresados es: " df[0].min())

print("Esto se hizo para el segundo commit en git")