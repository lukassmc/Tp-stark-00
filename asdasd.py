from funciones_stark import personaje_mas_alto
from data_stark import lista_personajes

altura_mas_alto , nombre_mas_alto= personaje_mas_alto(lista_personajes)


print(altura_mas_alto)
print(nombre_mas_alto)
# def nombre_mas_alto(lista: list):
#     altura_mas_alto= personaje_mas_alto(lista)
    
#     for heroe in lista:
        
#         altura_heroe= float(heroe["altura"])
#         if altura_heroe == altura_mas_alto:
#             heroe_mas_alto= heroe["nombre"]
#             break
        
#     return heroe_mas_alto

# '---------------------------------------*------------------------------------------'          

# def nombre_mas_bajo(lista: list):
#     altura_mas_bajo= personaje_mas_bajo(lista)
    
#     for heroe in lista:
#         altura_heroe= float(heroe["altura"])
#         if altura_heroe == altura_mas_bajo:
#             heroe_mas_bajo= heroe["nombre"]
        
#     return heroe_mas_bajo