from os import system
from funciones_stark00 import *

def pausar():
    system("pause")

def limpiar_terminal():
    system("cls")

def menu_superheroes()-> str:
    """Menu de opciones para obtener datos.

    Returns:
        str: Devuelve el dato de la opción elegida. 
    """
    limpiar_terminal()
    print("     Menu de opciones")
    print("A- Mostrar el nombre de todos los superheroes.")
    print("B- Mostrar el nombre y altura de todos los superheroes.")
    print("C- Mostrar la altura mayor")
    print("D- Mostrar la altura menor")
    print("E- Mostrar la altura promedio de todos los heroes")
    print("F- Mostrar Nombre del heroe con la mayor altura.")
    print("G- Mostrar Nombre del heroe con la menor altura.")
    print("H- Mostrar Heroe mas pesado.")
    print("I- Mostrar Heroe mas liviano.")
    print("J- Salir")
    
    return obtener_opcion("Ingrese una opcion:  ").lower()


def confirmar_salida(mensaje: str)-> bool:
    """Le pregunta al usuario si desea salir o no.

    Args:
        mensaje (str): Mensaje para preguntar si desea salir

    Returns:
        bool: Devuelve True si la opción es "Si"
    """
    respuesta= input(mensaje).lower()
    
    return respuesta == "si"



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
    
    lista_opciones= ["a","b","c","d","e","f","g","h","i","j"]
    
    while True:
        
        entrada = input(mensaje)
        if entrada in lista_opciones:
            
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
        
        case "a":
            
            print(nombres_superheroes(lista_personajes))
        
        case "b":
            
            print(nombre_y_altura_superheroes(lista_personajes))    
            
        case "c":
            
            print(f"La mayor altura es : {altura_maxima}")   
            flag_mas_alto= True
            
        case "d":
            
            print(f"La altura minima es : {altura_minima}")    
            
            flag_mas_bajo= True
            
        case "e":
          
            print(f"El promedio de alturas de todos los heroes es :{promedio_altura(lista_personajes)}")
              
        case "f":
            if flag_mas_alto:
                print(f"El nombre del heroe más alto es : {nombre_altura_maxima}")    
            else:
                print("Antes de saber el nombre, primero debes buscarlo en la opción C!")
            
        case "g":
            if flag_mas_bajo:
                print(f"El nombre del heroe más bajo es : {nombre_altura_minima}")
            else:
                print("Antes de sabre el nombre, debes buscarlo primero en la opción D")    
        case "h":
            
            print(f"El personaje mas pesado pesa {mayor_peso} y su nombre es {nombre_mas_pesado}")
                
        case "i":
            
            print(f"El Personaje mas liviano pesa {menor_peso}, y su nombre es {nombre_mas_liviano}")
        
        case "j":
            
            if confirmar_salida("Desea salir?\n "):
                break
            else:
                continue
        
    pausar()       
            
print("Fin del programa") 
        
            







