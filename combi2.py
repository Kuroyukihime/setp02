print("Coeficiente del Demonio 2.0")

import itertools    # Se importa la librería para crear combinaciones.

def combinatoria2(conjunto, k):    # Función que crea y guarda todas las conbinaciones posibles en una lista.
    combi = itertools.combinations(conjunto,k)    # Combi es donde se guardan todos las combinaciones que se pueden hacer con el conjunto y k.
    combifinal = []    # Se crea una lista vacía para luego retornar con las combinaciones.
    for elemento in combi:
        combifinal.append(elemento)    # Cada elemento de combi se agrega uno a uno a la lista combifinal.
    return (combifinal)    # Se retorna el resultado.

n = eval(input("Ingrese n: "))    # Se pide al usuario n, que es el valor total de los elementos a combinar.
if n <= 0:    # Si el número ingresado es menor o igual a cero se lanza una excepción porque no puede ser ninguno de esos valores.
    raise Exception("n debe ser mayor a 0.")
else:
    aux = []    # Se crea una lista vacía.
    print("Ingrese los elementos a combinar: ")
    while n!=0:    # El while retrocede hasta un n=0 para ingresar los datos que el usuario conto.
        elemento = input("Elemento: ")    # El elemento ingresado se guarda en elemento.
        aux.append(elemento)    # Elemento se agrega a la vez en una lista aux.
        n = n - 1    # El contador n disminuye en 1 a cada ciclo hasta llegar a cero.
    conjunto = set(aux)    # Se ingresa la lista aux a un conjunto.
    k = eval(input("Ingrese k: "))    # Se pide al usuario el valor k para calcular el total de elementos a combinar.
    if k > n and k < 0:    # Si el valor k ingresado es mayor a n o menor a cero se levanta una excepción.
        raise Exception("k debe ser menor a n y mayor o igual a 0.")
    else:
        print (combinatoria2(conjunto, k))    # Si no se llama a la función para calcular las combinaciones y se muestran en la misma.


