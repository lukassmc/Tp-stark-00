from data_stark import lista_personajes
from funciones_stark import *



#-------------------------------------* Nombre de superheroes * -----------------------------------------

print(f"{nombres_superheroes(lista_personajes)}")

#-------------------------------------* Nombre y altura * -----------------------------------------------

print(f"{nombre_y_altura_superheroes(lista_personajes)}")

#------------------------------------* Heroe Mas alto * -------------------------------------------------
altura_maxima , nombre_altura_maxima= personaje_mas_alto(lista_personajes)

print(f"La altura mas alta es : {altura_maxima} cm")

#------------------------------------* Heroe Mas Bajo * -------------------------------------------------
altura_minima , nombre_altura_minima= personaje_mas_bajo(lista_personajes)

print(f"La altura mas baja es {altura_minima} cm")

#------------------------------------* Promedio Altura * -----------------------------------------------

print(f"La altura promedio de todos los heroes es de {promedio_altura(lista_personajes)}")

#-----------------------------------* Nombre Heroe Mas Alto * ------------------------------------------

print(f"El heroe más alto es {nombre_altura_maxima}")

#-----------------------------------* Nombre Heroe Mas bajo * ------------------------------------------

print(f"El heroe más bajo es {nombre_altura_minima}")
