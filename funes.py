print("Funes el Memorioso.")

f = open('funes.txt', 'r')    # Este comando abre el archivo en modo lectura y lo guarda en f sin leer.
cadena = f.read()    # Se lee todo el texto de f y se guarda en cadena como string.
f.close()    # Se cierra el archivo 'funes'.
dicci = {}    # Se crea un diccionario vacío.
aux2 = []    # Se crea una lista aux2 vacía.
aux = cadena.split()    # La función split separa el string cadena en varios strings y los guarda en la lista aux.
for elemento in aux:    # El for recorre la lista aux por elemento.
    elemento = elemento.upper()    # La funcion upper vuelve a mayúcula el string elemento.
    aux2.append(elemento)    # Los elementos en mayúsculas son guardados en una segunda función auxiliar.
for elemento in aux2:    # El segundo for recorre la lista auxiliar 2.
    cont = aux2.count(elemento)    # La funcion count cuenta las veces que se repite un elemento en una lista y el valor se guarda en cont.
    dicci[elemento] = cont    # Dicci guarda la llave elemento con el valor cont, que sería la cantidad que el elemento se repite.

print(sorted(dicci.items(), key=lambda x: x[1], reverse=True))    # Esto ordena el diccionario por los valores de cada entrada del diccionario de mayor a menor.



