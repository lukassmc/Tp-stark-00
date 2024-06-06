from data_stark import *



'----------------------------------*-----------------------------------------------'
def nombres_superheroes(lista: list)-> list:
    """Guarda el nombre de todos los superheroes en una lista.

    Args:
        lista (list): lista de la que se extraen los nombres

    Returns:
        list: lista con todos los nombres de los superheroes
    """
    lista_retorno= []
    for el in lista:
        lista_retorno.append((el["nombre"]))
        
    return lista_retorno


'-------------------------------------*-------------------------------------------'
def nombre_y_altura_superheroes(lista: list)-> list:
    """Guarda el nombre y la altura de todos los superheroes en una lista

    Args:
        lista (list): lista de la que se extraen los datos

    Returns:
        list: lista con todos los datos requeridos
    """
    lista_retorno= []
    for el in lista:
        lista_retorno.append((el["nombre"]))
        lista_retorno.append((el["altura"]))
        
    return lista_retorno

'-------------------------------------*-------------------------------------------'

def personaje_mas_alto(lista: list):
    """Busca en la lista al personaje mas alto y guarda su altura y nombre en variables

    Args:
        lista (list): lista de la que se sacan los datos

    Returns:
        _type_: -
    """

    altura_heroe_mas_alto= 0
    
    for personaje in lista:
        altura= float(personaje["altura"])
        
        if altura > altura_heroe_mas_alto:
            
            altura_heroe_mas_alto= altura
            heroe_mas_alto= personaje["nombre"]
        

    
    return altura_heroe_mas_alto, heroe_mas_alto
            
'---------------------------------------*------------------------------------------'
    
def personaje_mas_bajo(lista: list):
    """Busca en la lista al personaje mas alto y guarda su altura y nombre en variables

    Args:
        lista (list): lista de la que se sacan los datos

    Returns:
        _type_:-
    """
    altura_heroe_mas_bajo= 0
    flag_menor= False
    
    
    for personaje in lista:
        altura= float(personaje["altura"])
        
        if flag_menor == False or altura  < altura_heroe_mas_bajo:
            
            altura_heroe_mas_bajo= altura
            heroe_mas_bajo= personaje["nombre"]
            
            flag_menor=True
        
    
    return altura_heroe_mas_bajo, heroe_mas_bajo
        
'---------------------------------------*------------------------------------------'       
    
def promedio_altura(lista: list)-> float:
    """Calcula el promedio de todas las alturas.

    Args:
        lista (list): lista de la que se sacan los datos

    Returns:
        float: El promedio de alturas
    """

    cantidad= len(lista)

    altura_total= 0
    for heroe in lista:
        altura= float(heroe["altura"])
        
        altura_total += altura
    
    return round((altura_total / cantidad), 2)

'---------------------------------------*------------------------------------------'          

def personaje_mas_pesado(lista: list):
    """Busca en la lista al personaje mas pesado y guarda su peso y nombre en variables

    Args:
        lista (list): lista de la que se sacan los datos

    Returns:
        _type_:-
    """
    mayor_peso= 0
    
    
    for personaje in lista:
        peso= float(personaje["peso"])
        
        if peso > mayor_peso:
            mayor_peso= peso
            heroe_mas_pesado= personaje["nombre"]

    return mayor_peso , heroe_mas_pesado


'---------------------------------------*------------------------------------------' 

def personaje_mas_liviano(lista: list):
    """Busca en la lista al personaje mas liviano y guarda su peso y nombre en variables

    Args:
        lista (list): lista de la que se sacan los datos

    Returns:
        _type_:-
    """
    
    menor_peso= 0
    flag_menor= False
    
    for personaje in lista:
        peso= float(personaje["peso"])
        
        if flag_menor == False or peso < menor_peso:
            menor_peso= peso
            heroe_mas_liviano= personaje["nombre"]
            flag_menor= True
    
    
    return menor_peso, heroe_mas_liviano

        
    












# > < \ 