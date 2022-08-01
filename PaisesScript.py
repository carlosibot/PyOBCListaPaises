lista = []

for x in range(0,5):
    lista.append(input("Introduzca un pais: "))

lista_arreglada = set(lista)
print(sorted(lista_arreglada))