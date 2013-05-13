print("Palindroma")

x = input("Ingrese un string: ")    # Se pide el string cualquiera al ususario y se guarda en x.
lista = list(x)    # El string es pasado a una lista.

def es_palindroma(lista):    # Función que retorna un True o False si el string es palindromo o no respectivamente.
    if lista[::1] == lista[::-1]:    # Si la lista en orden es igual a la lista al revés se retorna un True.
        return True
    else:
        return False    # Si no lo es retorna un False.

print(es_palindroma(lista))    # Se muestran inmediatamente los valores retornados.
