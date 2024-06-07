from data_stark import * 
from funciones_stark00 import *


def mapear_campo(funcion, lista: list) -> list:
    validar_lista(lista)
    lista_retorno = []
    for el in lista :
        lista_retorno.append(funcion(el))
    return lista_retorno


def filtrar_lista(filtro, lista:list)->list:
    validar_lista(lista)
    
    lista_retorno = []
    for el in lista:
        if filtro(el):
            lista_retorno.append(el)
    return lista_retorno




def contador_elem_in_dict(campo, lista:list):
    validar_lista(lista)
    
    diccionario = {}
    for campo in lista:
        
        if campo in diccionario:
            diccionario[campo] += 1
        else:
            diccionario[campo] = 1
    return diccionario


def sin_inteligencia(lista: list):
    validar_lista(lista)
    
    for valor in lista:
        if valor["inteligencia"] == "":
            valor["inteligencia"] = "no tiene"


def contador_ineligencias(lista):
    validar_lista(lista)
    
    inteligencias= {}
    for tipo in lista:
        if tipo in lista:
            inteligencias[tipo] += 1
        elif tipo == "":
            inteligencias["No Tiene"] = 1
        else:
            inteligencias[tipo] = 1




def agrupar_campos(campo_a_ordenar, lista: list):
    """agrupa los superheroes por color de ojos

    Args:
        campo_a_ordenar (_type_): campo que se decide ordenar
        lista (list): lista que coniene los datos a comparar

    Returns:
        _type_: diccionario con los valores 
    """
    validar_lista(lista)
    
    diccionario = {}
    for color in lista:
        diccionario[color]= []
    for i in range(len(lista)):
        diccionario[lista[i]].append(campo_a_ordenar[i])
        
    return diccionario

    
    
    
    

"------------------------------------------------* A *----------------------------------"
superheroes_m= mapear_campo(lambda nombre: nombre["nombre"] , filtrar_lista(lambda genero: genero["genero"]== "M"   , lista_personajes))
print(superheroes_m)

"------------------------------------------------* B *----------------------------------"
superheroes_f= mapear_campo(lambda nombre: nombre["nombre"] , filtrar_lista(lambda genero: genero["genero"]== "F"   , lista_personajes))
print(superheroes_m)

"------------------------------------------------* C *----------------------------------"
lista_heroes_m= filtrar_lista(lambda filtro_m: filtro_m["genero"] == "M" ,   lista_personajes)

heroe_mas_alto, nombre_heroe_mas_alto= personaje_mas_alto(lista_heroes_m)

print(heroe_mas_alto)
print(nombre_heroe_mas_alto)

"------------------------------------------------* D *----------------------------------"

lista_heroeinas_f= filtrar_lista(lambda filtro_f: filtro_f["genero"]== "F", lista_personajes)

heroina_mas_alta, nombre_heroina_mas_alta= personaje_mas_alto(lista_heroeinas_f)
print(heroina_mas_alta)
print(nombre_heroina_mas_alta)
"------------------------------------------------* E *----------------------------------"

heroe_mas_bajo, nombre_heroe_mas_bajo= personaje_mas_bajo(lista_heroes_m)
print(heroe_mas_bajo)
print(nombre_heroe_mas_bajo)
"------------------------------------------------* F *----------------------------------"

heroina_mas_baja, nombre_heroina_mas_baja= personaje_mas_bajo(lista_heroeinas_f)
print(heroina_mas_baja)
print(nombre_heroina_mas_baja)
"------------------------------------------------* G *----------------------------------"

promedio_altura_heroes= promedio_altura(lista_heroes_m)
print(promedio_altura_heroes)
"------------------------------------------------* H *----------------------------------"

promedio_altura_heroinas= promedio_altura(lista_heroeinas_f)
print(promedio_altura_heroinas)
"------------------------------------------------* J *----------------------------------"

lista_colores_de_ojos= mapear_campo(lambda heroe: heroe["color_ojos"], lista_personajes)


print(contador_elem_in_dict("color_ojos", lista_colores_de_ojos))

"------------------------------------------------* K *----------------------------------"

lista_colores_de_pelo= mapear_campo(lambda heroe: heroe["color_pelo"], lista_personajes)

print(contador_elem_in_dict("color_pelo", lista_colores_de_pelo))

"------------------------------------------------* L *----------------------------------"

sin_inteligencia(lista_personajes)
lista_tipo_inteligencia= mapear_campo(lambda heroe: heroe.get("inteligencia", "No Tiene"), lista_personajes)
print(contador_elem_in_dict("inteligencia", lista_tipo_inteligencia))


"------------------------------------------------* M *----------------------------------"
nombres_heroes= mapear_campo(lambda nombre: nombre["nombre"], lista_personajes)

print(agrupar_campos(nombres_heroes, lista_colores_de_ojos))

"------------------------------------------------* N *----------------------------------"
print(agrupar_campos(nombres_heroes, lista_colores_de_pelo))

"------------------------------------------------* O *----------------------------------"
print(agrupar_campos(nombres_heroes, lista_tipo_inteligencia))