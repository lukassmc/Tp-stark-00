from data_stark import *



'----------------------------------*-----------------------------------------------'
def nombres_superheroes(lista: list):
    lista_retorno= []
    for el in lista:
        lista_retorno.append((el["nombre"]))
        
    return lista_retorno


'-------------------------------------*-------------------------------------------'
def nombre_y_altura_superheroes(lista: list):
    lista_retorno= []
    for el in lista:
        lista_retorno.append((el["nombre"]))
        lista_retorno.append((el["altura"]))
        
    return lista_retorno

'-------------------------------------*-------------------------------------------'

def personaje_mas_alto(lista: list):
    altura_heroe_mas_alto= 0
    for personaje in lista:
        altura= float(personaje["altura"])
        if altura > altura_heroe_mas_alto:
            
            altura_heroe_mas_alto= altura
            heroe_mas_alto= personaje["nombre"]
        

    
    return altura_heroe_mas_alto, heroe_mas_alto
            
'---------------------------------------*------------------------------------------'
    
def personaje_mas_bajo(lista: list):
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
    
def promedio_altura(lista: list):
    contador_heroes= 0
    altura_total= 0
    for heroe in lista:
        altura= float(heroe["altura"])
        
        contador_heroes += 1
        altura_total += altura
    
    return (altura_total // contador_heroes)

'---------------------------------------*------------------------------------------'          















# > < \ 