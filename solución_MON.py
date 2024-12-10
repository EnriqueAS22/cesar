from typing import *

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
LONGITUD_ALFABETO = len(ALFABETO)

def cifrar(mensaje:str,d:int)->str:
    pasos = 0
    punto_inicio = 0
    mensaje_cifrado=''
    for letra in mensaje.upper():
        if letra in ALFABETO:

            punto_inicio = ALFABETO.find(letra)
            pasos = punto_inicio + d
            # print(pasos)
            # while pasos > LONGITUD_ALFABETO:
            #     pasos -= LONGITUD_ALFABETO
            pasos = pasos % LONGITUD_ALFABETO
            mensaje_cifrado += ALFABETO[pasos]
    return mensaje_cifrado

def creaCifrador(dist:int)->Callable:
    def cifrador(mensaje: str) -> str:
        return cifrar(mensaje, dist)
    return cifrador

def creaParCesar(dist:int)->Tuple[Callable,Callable]:
    def cifrador(mensaje: str) -> str:
        return cifrar(mensaje, dist)
    
    def descifrador(mensaje: str) -> str:
        return cifrar(mensaje, -dist)

    return cifrador, descifrador

"""
Para comprobar los resultados hacemos distintos assert
"""
# Para la función cifrar
assert cifrar("zig", 3) == "BLJ"
assert cifrar("blj", -3) == "ZIG"

# Para la función creaCifrador, que tiene cifrador dentro
cifrador2 = creaCifrador(2)

assert cifrador2("A Z") == "CBA"

# Para la función creaParCesar, que tiene cifrador y descifrador dentro
cifra2, descifra2 = creaParCesar(2)

assert cifra2("A Z") == "CBA"
assert descifra2("CBA") == "A Z"