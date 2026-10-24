"""Tus pruebas: mínimo 2 por función, sobre casos que el contrato NO cubre
(un solo elemento, todos iguales, árbol degenerado, k negativo, ...).
Cada prueba lleva un comentario de una línea: qué caso cubre y por qué importa.
"""
from estructuras import ListaDoble, ABB
from solucion import quitar_repetidos, posicion_en_ranking


def test_quitar_repetidos_un_solo_elemento():
    # Un solo nodo: no hay nada que quitar.
    lista = ListaDoble([4])
    assert quitar_repetidos(lista) == 0
    assert list(lista) == [4]

def test_quitar_repetidos_todos_iguales():
    # Todos iguales: debe quedar un solo nodo.
    lista = ListaDoble([9, 9, 9])
    assert quitar_repetidos(lista) == 2
    assert list(lista) == [9]

def test_ranking_k_negativo():
    # k negativo no es un puesto válido.
    assert posicion_en_ranking(ABB([10, 20]), -1) is None

def test_ranking_arbol_degenerado():
    # Árbol degenerado: el último puesto es el menor.
    assert posicion_en_ranking(ABB([30, 20, 10]), 3) == 10
