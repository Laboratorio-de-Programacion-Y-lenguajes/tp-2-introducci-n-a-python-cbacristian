# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split(" ")
    resultado = " ".join(palabra.capitalize() if palabra else "" for palabra in palabras)
    print(resultado)
    return resultado
    pass

def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = set("aeiou")
    return sum(1 for char in texto.lower() if char in vocales)
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    desplazamiento = desplazamiento % 26
    resultado = []
    for char in texto:
        if 'a' <= char <= 'z':
            resultado.append(chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            resultado.append(chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A')))
        else:
            resultado.append(char)
    return ''.join(resultado)
    pass
