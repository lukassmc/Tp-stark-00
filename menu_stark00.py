from os import system
from funciones_stark00 import *
from funciones_stark01 import *


def pausar():
    system("pause")

def limpiar_terminal():
    system("cls")

def menu_superheroes():
    """Menu de opciones para obtener datos.

    Returns:
        str: Devuelve el dato de la opción elegida. 
    """
    limpiar_terminal()
    print("     Menu de opciones")
    print("1- Mostrar el nombre de todos los superheroes.")
    print("2- Mostrar el nombre y altura de todos los superheroes.")
    print("3- Mostrar la altura mayor")
    print("4- Mostrar la altura menor")
    print("5- Mostrar la altura promedio de todos los heroes")
    print("6- Mostrar Nombre del heroe con la mayor altura.")
    print("7- Mostrar Nombre del heroe con la menor altura.")
    print("8- Mostrar Heroe mas pesado.")
    print("9- Mostrar Heroe mas liviano.")
    print("10- Mostrar Nombre superheroes Masculinos.")
    print("11- Mostrar nombre superheroes femeninos.")
    print("12- Mostrar superheroe masculino más alto.")
    print("13- Mostrar superheroe femenino más alto.")
    print("14- Mostrar superheroe masculino más bajo.")
    print("15- Mostrar superheroe femenino más bajo.")
    print("16- Mostrar altura promedio de los superheroes Masculinos.")
    print("17- Mostrar altura promedio de los superheroes Femeninos.")
    print("18- Mostrar cantidad de heroes con cada tipo de color de ojos.")
    print("19- Mostrar cantidad de heroes con cada tipo de color de ojos.")
    print("20- Mostrar cantidad de heroes con cada tipo de inteligencia.")
    print("21- Mostrar superheroes agrupados por color de ojos.")
    print("22- Mostrar superheroes agrupados por color de pelo.")
    print("23- Mostrar superheroes agrupados por inteligencia.")
 
   
    print("24- Salir")
    
    return obtener_opcion("Ingrese una opcion:  ")


def confirmar_salida(mensaje: str)-> bool:
    """Le pregunta al usuario si desea salir o no.

    Args:
        mensaje (str): Mensaje para preguntar si desea salir

    Returns:
        bool: Devuelve True si la opción es "Si"
    """
    respuesta= input(mensaje).lower()
    
    return respuesta == "si"


def es_numero(entrada)-> bool:
    """Verifica si es un int

    Args:
        entrada (_type_): Valor de entrada

    Returns:
        _type_: Devuelve True si es un int, de lo contrario False
    """
    flag_es_numero= False
    
    try:
        
        int(entrada) 
        flag_es_numero= True
    
    except ValueError:
        
        flag_es_numero= False
        
    return flag_es_numero

def es_texto(entrada)-> bool:
    """Verifica si es str

    Args:
        entrada (_type_): Valor de entrada

    Returns:
        bool: devuelve true si es str
    """
    return isinstance(entrada, str)



def obtener_opcion(mensaje):
    """Valida que la opción ingresada esté dentro de las opciones validas.

    Args:
        mensaje (_type_): mensaje para pedir el dato

    Returns:
        _type_: -
    """
    
   
    
    while True:
        
        entrada = int(input(mensaje))
        
        if entrada > 0 or entrada < 25:
            
            return entrada
        else:
            print("Entrada inválida. Por favor, ingrese una opción válida.")
            

flag_mas_alto= False
flag_mas_bajo= False

altura_maxima , nombre_altura_maxima= personaje_mas_alto(lista_personajes)
altura_minima , nombre_altura_minima= personaje_mas_bajo(lista_personajes)


mayor_peso , nombre_mas_pesado = personaje_mas_pesado(lista_personajes)
menor_peso , nombre_mas_liviano = personaje_mas_liviano(lista_personajes)

while True:
    
    
    match menu_superheroes():
        
        case 1:
            
            print(nombres_superheroes(lista_personajes))
        
        case 2:
            
            print(nombre_y_altura_superheroes(lista_personajes))    
            
        case 3:
            
            print(f"La mayor altura es : {altura_maxima}")   
            flag_mas_alto= True
            
        case 4:
            
            print(f"La altura minima es : {altura_minima}")    
            
            flag_mas_bajo= True
            
        case 5:
          
            print(f"El promedio de alturas de todos los heroes es :{promedio_altura(lista_personajes)}")
              
        case 6:
            if flag_mas_alto:
                print(f"El nombre del heroe más alto es : {nombre_altura_maxima}")    
            else:
                print("Antes de saber el nombre, primero debes buscarlo en la opción C!")
            
        case 7:
            if flag_mas_bajo:
                print(f"El nombre del heroe más bajo es : {nombre_altura_minima}")
            else:
                print("Antes de sabre el nombre, debes buscarlo primero en la opción D")    
        case 8:
            
            print(f"El personaje mas pesado pesa {mayor_peso} y su nombre es {nombre_mas_pesado}")
                
        case 9:
            
            print(f"El Personaje mas liviano pesa {menor_peso}, y su nombre es {nombre_mas_liviano}")
            
        case 10:
              superheroes_m= mapear_campo(lambda nombre: nombre["nombre"] , filtrar_lista(lambda genero: genero["genero"]== "M"   , lista_personajes))
              print(superheroes_m)
            
        case 11:
            
            superheroes_f= mapear_campo(lambda nombre: nombre["nombre"] , filtrar_lista(lambda genero: genero["genero"]== "F"   , lista_personajes))
            print(superheroes_f)
        case 12:
            
            lista_heroes_m= filtrar_lista(lambda filtro_m: filtro_m["genero"] == "M" ,   lista_personajes)

            heroe_mas_alto, nombre_heroe_mas_alto= personaje_mas_alto(lista_heroes_m)

            print(heroe_mas_alto)
            print(nombre_heroe_mas_alto)
        case 13:
            
            lista_heroeinas_f= filtrar_lista(lambda filtro_f: filtro_f["genero"]== "F", lista_personajes)

            heroina_mas_alta, nombre_heroina_mas_alta= personaje_mas_alto(lista_heroeinas_f)
            print(heroina_mas_alta)
            print(nombre_heroina_mas_alta)
        case 14:
            
            heroe_mas_bajo, nombre_heroe_mas_bajo= personaje_mas_bajo(lista_heroes_m)
            print(heroe_mas_bajo)
            print(nombre_heroe_mas_bajo)
            
        case 15:
            
            heroina_mas_baja, nombre_heroina_mas_baja= personaje_mas_bajo(lista_heroeinas_f)
            print(heroina_mas_baja)
            print(nombre_heroina_mas_baja)
        case 16:
            
            promedio_altura_heroes= promedio_altura(lista_heroes_m)
            print(promedio_altura_heroes)
        case 17:
            
            promedio_altura_heroinas= promedio_altura(lista_heroeinas_f)
            print(promedio_altura_heroinas)
        case 18:
            lista_colores_de_ojos= mapear_campo(lambda heroe: heroe["color_ojos"], lista_personajes)


            print(contador_elem_in_dict("color_ojos", lista_colores_de_ojos))
        case 19:
            
            lista_colores_de_pelo= mapear_campo(lambda heroe: heroe["color_pelo"], lista_personajes)

            print(contador_elem_in_dict("color_pelo", lista_colores_de_pelo))
        case 20:
            
            sin_inteligencia(lista_personajes)
            lista_tipo_inteligencia= mapear_campo(lambda heroe: heroe.get("inteligencia", "No Tiene"), lista_personajes)
            print(contador_elem_in_dict("inteligencia", lista_tipo_inteligencia))
            
        case 21:
            
            nombres_heroes= mapear_campo(lambda nombre: nombre["nombre"], lista_personajes)

            print(agrupar_campos(nombres_heroes, lista_colores_de_ojos))
        case 22:
            
           print(agrupar_campos(nombres_heroes, lista_colores_de_pelo))
        case 23:
            
           print(agrupar_campos(nombres_heroes, lista_tipo_inteligencia))
        
        case 24:
            
            if confirmar_salida("Desea salir?\n "):
                break
            else:
                continue
        
    pausar()      
  
            
print("Fin del programa") 
        
            







