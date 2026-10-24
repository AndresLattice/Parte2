"""Prueba individual · Estructuras de Datos · Parte II

Nombre: Andres David Agudelo Henao   Documento: 1011395989

Metodología del curso (SDD): la especificación manda. El contrato exacto de
cada función está en test_contrato.py. Léelo ANTES de programar: lo que no
diga el enunciado, lo dicen esas pruebas.

Reglas: recorre los nodos (cabeza, cola, siguiente, anterior, raiz, izquierdo,
derecho). No conviertas la estructura completa a una lista de Python.
Escribe en un comentario la complejidad Big-O de cada función y por qué.
"""
from estructuras import ListaDoble, ABB


def quitar_repetidos(lista: ListaDoble) -> int:
    """Quita los datos repetidos: al terminar, cada dato aparece una sola vez en la lista.
    Devuelve cuántos nodos se eliminaron.
    """
    # O(n): un recorrido desde la cola; set y eliminar_nodo son O(1).
    vistos = set()
    eliminados = 0
    actual = lista.cola
    while actual is not None:
        anterior = actual.anterior
        if actual.dato in vistos:
            lista.eliminar_nodo(actual)
            eliminados = eliminados + 1
        else:
            vistos.add(actual.dato)
        actual = anterior
    return eliminados


def posicion_en_ranking(arbol: ABB, k: int):
    """El árbol guarda los puntajes de una competencia.
    Devuelve el puntaje que ocupa el puesto k del ranking.
    """
    # O(h + k): inorden al revés que para en el puesto k; h es la altura.
    if k < 1 or k > len(arbol):
        return None
    contador = [0]

    def buscar(nodo):
        if nodo is None:
            return None
        encontrado = buscar(nodo.derecho)
        if encontrado is not None:
            return encontrado
        contador[0] = contador[0] + 1
        if contador[0] == k:
            return nodo.dato
        return buscar(nodo.izquierdo)

    return buscar(arbol.raiz)
