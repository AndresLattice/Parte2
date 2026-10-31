# Prueba individual · Estructuras de Datos

**Universidad Cooperativa de Colombia · Momento 2 (semanas 7–12) · 12 % del curso · 90 minutos**

Nombre: Andres David Agudelo Henao
Documento: 1011395989

## Instrucciones

- La prueba tiene dos partes. **Parte I** (35 min, 40 puntos): respondes en este mismo archivo, debajo de cada pregunta, y lo subes a D2L. **Parte II** (55 min, 60 puntos): se publica en D2L cuando cierra la Parte I.
- Sin internet, sin IA y sin ejecutar código en la Parte I.
- Todas las estructuras son **las que construimos en clase con nodos**: `Nodo(dato, siguiente)`, `NodoDoble(dato, anterior, siguiente)` y `NodoArbol(dato, izquierdo, derecho)`. Responde con lo que hacen **nuestros nodos**, no con listas de Python ni con lo que dice un libro.
- Cada pregunta pide una **justificación**. Sin ella, la respuesta vale la mitad.
- Si una expresión no se puede evaluar, escribe qué error produce y por qué.
- Si una pregunta trata un tema que **no vimos en clase**, escribe **«No lo vimos en clase»**. Es una respuesta válida y no te resta puntos.

---

# Parte I · Seguir los nodos (40 puntos)

## 1. Nodos de la lista doble (8 pts)

Se tienen cuatro `NodoDoble` enlazados en los dos sentidos:

```
cabeza                                cola
  [10] ⇄ [20] ⇄ [30] ⇄ [40]
```

`cabeza.anterior` es `None` y `cola.siguiente` es `None`. Alguien escribe este código para insertar el 55:

```python
n = cabeza.siguiente
nuevo = NodoDoble(55, n, n.siguiente)
n.siguiente = nuevo
```

a) ¿Qué dato tiene el nodo `n`?  
b) Escribe el recorrido que se obtiene empezando en `cabeza` y avanzando por `siguiente` hasta `None`. Luego escribe el que se obtiene empezando en `cola` y retrocediendo por `anterior` hasta `None`.  
c) ¿Cuánto vale `cola.anterior.anterior.dato`?  
d) ¿Qué línea le falta al código para que la inserción quede correcta? Escríbela.

Justificación: explica por qué en b) los dos recorridos no muestran lo mismo.

**Respuesta:**

A = 20                                 
B = hacia adelante 10, 20, 55, 30, 40 / hacia atras 40, 30, 20, 10 / Se salta el 55 porque para atras no hay nada que lo conecte, la tercera linea solo apunta el 30 con el 55 de izquierda a derecha.    
C = Vale 20 porque la cola es el 40 y el anterior dos veces hacia atras es el 20  
D = Si con correcta es que quede completo para que no pase lo del punto B, que se salta el 55, habria simplemente que conectar la cola con el nuevo 
```python
nuevo.siguiente.anterior = nuevo
```

---

## 2. Nodos de la pila (6 pts)

En una `PilaEnlazada` del curso vacía se ejecuta:

`push(1)` · `push(2)` · `push(3)` · `pop()` · `push(9)` · `push(4)`

Sea `t = pila._tope`.

a) ¿Qué devolvió el `pop()`?  
b) ¿Cuánto vale `t.dato`? ¿Y `t.siguiente.dato`? ¿Y `t.siguiente.siguiente.siguiente.dato`?  
c) ¿Qué es `t.siguiente.siguiente.siguiente.siguiente`?

Justificación: dibuja la cadena de nodos con sus flechas `siguiente` y explica hacia dónde apuntan.

**Respuesta:**

A = 3 / porque hasta ese momento el tope era 3  
B = 4, 9, 1 /  4 porque el ultimo numero que se ingreso fue el 4, 9 porque se avanza a la izquierda con el siguiente osea el 9, y 1 porque pasa porque se pide recorrer 3 a la izquierda 4/-9-2-1 el 3 se omite porque se saco con el pop de antes
C = None porque ya no hay nada a la izquierda 



---

## 3. Nodos de la cola (6 pts)

En una `ColaEnlazada` del curso vacía se ejecuta:

`encolar(5)` · `encolar(6)` · `desencolar()` · `encolar(7)` · `desencolar()` · `desencolar()`

a) ¿Qué devolvió cada `desencolar()`?  
b) Al terminar, ¿a qué apuntan `_cabeza` y `_cola`?  
c) Ahora se ejecuta `encolar(8)`. ¿Cuánto vale `_cabeza.dato`? ¿`_cabeza is _cola` da `True` o `False`?  
d) Repite c) suponiendo que en `desencolar` alguien **borró** la línea `self._cola = None`. ¿Qué pasa con el 8?

Justificación de d).

**Respuesta:**

A = Devolvieron 6, 5 y 7 / los devuelve en el orden en el que entraron
B = cabeza y cola quedaron en None porque antes ya se habian sacado los datos que habian, 5, 6, 7
C = 8 y da true, porque al agregar solo 1 dato se vuelve la cabeza y la cola, por eso tambien da true  
D =   No se :(

---

## 4. Nodos del ABB (10 pts)

En un `ABB` del curso vacío se insertan, en este orden:

`50, 30, 70, 25, 40, 60, 80, 40, 30, 45`

Sea `r = arbol.raiz`.

a) Dibuja el árbol (en texto, como en clase).  
b) ¿Cuánto valen `len(arbol)` y `arbol.altura()`? ¿Cuál es la altura de un `ABB` vacío?  
c) ¿Cuánto valen `r.izquierdo.derecho.derecho.dato` y `r.izquierdo.derecho.izquierdo.dato`?  
d) Escribe el recorrido inorden.  
e) Se elimina el 30. ¿Cuánto vale ahora `r.izquierdo.dato`? Escribe el preorden.

Justificación: explica tu respuesta a `len(arbol)`.

**Respuesta:**

A = 
```python
          50
         /  \
        /    \
      30      70
     /  \    /  \  
   25   40  60  80
          \
          45
```

B = len vale 8, altura es 3 y la altura de un ABB vacio es 0 / Son 8 datos los que hay en el arbol, los duplicados no cuentan, altura es 4 porque va de 50 a 45   
C =  r.izquierdo.derecho.derecho.dato vale 45 y el r.izquierdo.derecho.izquierdo.dato da none  
D = 25, 30, 40, 45, 50, 60, 70, 80 / basicamente de menor a mayor  
E = r.izquierdo.dato es 40 / 50, 40, 25, 45, 70, 60, 80.
```python
          50
        /    \
      40      70
     /  \    /  \
   25   45  60  80
```

---

## 5. Nodos de la lista circular (6 pts)

Cinco `Nodo` forman una lista **circular** simple: `1 → 2 → 3 → 4 → 5 → 1` (el `siguiente` del 5 es el 1). La variable `inicio` apunta al nodo del 1. Se ejecuta:

```python
actual = inicio
while actual.siguiente is not actual:
    victima = actual.siguiente
    actual.siguiente = victima.siguiente
    actual = actual.siguiente
```

a) ¿En qué orden salen de la lista los nodos (`victima.dato` en cada vuelta)?  
b) Al terminar, ¿cuánto vale `actual.dato`?  
c) Al terminar, ¿`actual.siguiente is actual` da `True` o `False`? ¿Por qué?  
d) Si la condición del ciclo fuera `while actual is not None:`, ¿qué pasaría?  

Justificación: dibuja el círculo de nodos después de la segunda vuelta.

**Respuesta:**

A = victima.dato 2, 4, 1, 5 
B = 3 porque es el unico que no salio 
C = True el 3 quedo apuntandose a si mismo, el siguiente de el mismo sigue siendo el  
D = el ciclo no tendria fin

```python
    [1] -> [3] -> [5]
     ^             |
     ---------------
```

---

## 6. Recorrer nodos (4 pts)

Una `ListaDoble` del curso tiene 1000 elementos. ¿Cuántas veces se pasa de un nodo a otro (`actual = actual.siguiente` o `actual = actual.anterior`) para ejecutar:

a) `obtener(993)` 
b) `obtener(12)`

Justificación: ¿desde qué nodo arranca cada recorrido y por qué?

**Respuesta:**

A = Son 6 pasos actual = actual.anterior
B = Son 12 pasos actual = actual.siguiente

---

## 7. Lista doble con nodo centinela

Una `ListaDoble` también se puede implementar con un **nodo centinela**.

a) ¿Qué es el nodo centinela y qué dato guarda?
b) ¿Qué ventaja tiene frente a manejar `cabeza` y `cola` por separado?
c) Escribe cómo quedaría `insertar_al_final(dato)` usando el centinela.

**Respuesta:**

No lo vimos en clase :(

---

## 8. Lista de saltos (skip list)

Una lista de saltos guarda `10, 20, 30, 40, 50, 60, 70` en el nivel 0. En el nivel 1 están `20, 40, 60` y en el nivel 2 está solo `40`. Cada nodo tiene una referencia `adelante[i]` por cada nivel en el que aparece.

a) Describe, nodo por nodo, cómo se busca el 50 empezando por el nivel más alto.  
b) ¿Qué complejidad promedio tiene la búsqueda y por qué?  
c) ¿Cómo se decide en cuántos niveles queda un nodo nuevo al insertarlo?

**Respuesta:**

No lo hemos visto (creo :D)



---

# Parte II · Implementación con nodos (60 puntos)

Descarga `Parte_II.zip` de D2L. Contiene:

- `estructuras.py`: `ListaDoble` (con `cabeza` y `cola`) y `ABB`, ya completas. **No lo modifiques.**
- `solucion.py`: las dos funciones que implementas.
- `test_contrato.py`: **el contrato**. Léelo antes de programar: lo que el enunciado no diga, lo dicen esas pruebas. No se modifica.
- `test_mias.py`: tus pruebas.

### Ejercicio 1 · `quitar_repetidos(lista)` (30 pts)
Quita los datos repetidos de una `ListaDoble`: al terminar, cada dato aparece una sola vez. Devuelve cuántos nodos eliminó.

### Ejercicio 2 · `posicion_en_ranking(arbol, k)` (30 pts)
El `ABB` guarda los puntajes de una competencia. Devuelve el puntaje que ocupa el puesto `k` del ranking.

### Reglas
- Recorre los nodos (`cabeza`, `cola`, `siguiente`, `anterior`, `raiz`, `izquierdo`, `derecho`). **No conviertas la estructura completa a una lista de Python.**
- Escribe en un comentario la complejidad Big-O de cada función y por qué.
- En `test_mias.py` escribe mínimo 2 pruebas por función sobre casos que el contrato **no** cubre, cada una con un comentario de qué caso cubre.
- Ejecuta `python -m pytest -v` hasta que todo pase.
- Sube a D2L `solucion.py` y `test_mias.py`.

| Criterio (por ejercicio) | Peso |
|---|---|
| Cumple el contrato y la estructura queda bien | 45 % |
| Casos extremos y tus pruebas | 25 % |
| Complejidad adecuada y declarada | 20 % |
| Claridad | 10 % |
