from data_stark import *

def validar_lista(lista):
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

'----------------------------------*-----------------------------------------------'

def nombres_superheroes(lista: list) -> list:
    """Guarda el nombre de todos los superheroes en una lista.
    Args:
        lista (list): lista de la que se extraen los nombres
    Returns:
        list: lista con todos los nombres de los superheroes
    """
    validar_lista(lista)
    lista_retorno = [el["nombre"] for el in lista]
    return lista_retorno

'-------------------------------------*-------------------------------------------'
def nombre_y_altura_superheroes(lista: list) -> list:
    """Guarda el nombre y la altura de todos los superheroes en una lista
    Args:
        lista (list): lista de la que se extraen los datos
    Returns:
        list: lista con todos los datos requeridos
    """
    validar_lista(lista)
    lista_retorno = [(el["nombre"], el["altura"]) for el in lista]
    return lista_retorno

'-------------------------------------*-------------------------------------------'
def personaje_mas_alto(lista: list):
    """Busca en la lista al personaje mas alto y guarda su altura y nombre en variables
    Args:
        lista (list): lista de la que se sacan los datos
    Returns:
        tuple: Altura y nombre del personaje más alto
    """
    validar_lista(lista)
    altura_heroe_mas_alto = 0
    heroe_mas_alto = ""

    for personaje in lista:
        altura = float(personaje["altura"])
        if altura > altura_heroe_mas_alto:
            altura_heroe_mas_alto = altura
            heroe_mas_alto = personaje["nombre"]

    return altura_heroe_mas_alto, heroe_mas_alto

'---------------------------------------*------------------------------------------'
def personaje_mas_bajo(lista: list):
    """Busca en la lista al personaje mas alto y guarda su altura y nombre en variables
    Args:
        lista (list): lista de la que se sacan los datos
    Returns:
        tuple: Altura y nombre del personaje más bajo
    """
    validar_lista(lista)
    altura_heroe_mas_bajo = float('inf')
    heroe_mas_bajo = ""

    for personaje in lista:
        altura = float(personaje["altura"])
        if altura < altura_heroe_mas_bajo:
            altura_heroe_mas_bajo = altura
            heroe_mas_bajo = personaje["nombre"]

    return altura_heroe_mas_bajo, heroe_mas_bajo

'---------------------------------------*------------------------------------------'
def promedio_altura(lista: list) -> float:
    """Calcula el promedio de todas las alturas.
    Args:
        lista (list): lista de la que se sacan los datos
    Returns:
        float: El promedio de alturas
    """
    validar_lista(lista)
    cantidad = len(lista)
    altura_total = sum(float(heroe["altura"]) for heroe in lista)
    return round((altura_total / cantidad), 2)

'---------------------------------------*------------------------------------------'
def personaje_mas_pesado(lista: list):
    """Busca en la lista al personaje mas pesado y guarda su peso y nombre en variables
    Args:
        lista (list): lista de la que se sacan los datos
    Returns:
        tuple: Peso y nombre del personaje más pesado
    """
    validar_lista(lista)
    mayor_peso = 0
    heroe_mas_pesado = ""

    for personaje in lista:
        peso = float(personaje["peso"])
        if peso > mayor_peso:
            mayor_peso = peso
            heroe_mas_pesado = personaje["nombre"]

    return mayor_peso, heroe_mas_pesado

'---------------------------------------*------------------------------------------'
def personaje_mas_liviano(lista: list):
    """Busca en la lista al personaje mas liviano y guarda su peso y nombre en variables
    Args:
        lista (list): lista de la que se sacan los datos
    Returns:
        tuple: Peso y nombre del personaje más liviano
    """
    validar_lista(lista)
    menor_peso = float('inf')
    heroe_mas_liviano = ""

    for personaje in lista:
        peso = float(personaje["peso"])
        if peso < menor_peso:
            menor_peso = peso
            heroe_mas_liviano = personaje["nombre"]

    return menor_peso, heroe_mas_liviano
