# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    return [func(elemento) for elemento in lista]
    pass


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    def compuesta(*args, **kwargs):
        return f(g(*args, **kwargs))
    return compuesta
    pass


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]
        resultado = func(*args, **kwargs)
        cache[key] = resultado
        return resultado

    return wrapper
    pass


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    acumulado = inicial
    for elemento in lista:
        acumulado = func(acumulado, elemento)
    return acumulado
    pass
