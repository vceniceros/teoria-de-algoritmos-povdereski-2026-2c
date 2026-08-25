# ejercicios de hoy



## ejercicio 4 de la guia

En un tablero de ajedrez (una cuadrícula de 8x8) se ubica la pieza llamada “caballo”
en la esquina superior izquierda. Un caballo tiene una manera peculiar de moverse por el
tablero: Dos casillas en dirección horizontal o vertical y después una casilla más en
ángulo recto (formando una forma similar a la letra “L”). El caballo se traslada de la casilla
inicial a la final sin tocar las intermedias, dado que las “salta”. Se quiere determinar si es
posible, mover esta pieza de forma sucesiva a través de todas las casillas del tablero,
pasando una sola vez por cada una de ellas, y terminando en la casilla inicial. Plantear la
solución mediante backtracking.

1. identificamos como se mueve un caballo y definimos 

el punto de busqueda exaustiva es probar TODAS las posibles soluciones (al menos en el peor de los escenarios)

1. empezamos desde el (0,0)

```
        (0,0)
        /   \
    (2,1)   (1,2)

y asi para cada estado posible
```

tenemos para empezar 8 estados potenciales (los movimientos posibles del caballo) elevado a 64 (el tablero es 8 * 8) o sea tenemos potencialmente 8⁶4 

funcion de movimientos

```python
def move(x,y):
    moves = []
    if x < 6 and y < 7:
        moves.append((x+2, y + 1))
    if x < 7 and y > 0:
        moves.append((x + 2, y - y))
    ## todas las combinaciones validas
    return moves
```

eso es O(1) (son siempre 8 if's)

funcion de recorrer el arbol

```python
def tour(x,y, visitados):
    moves = moves(x,y)
    for(m_x, m_y) in moves
        if(m_x, m_y) in visitados:
            continue
        visitados.add(m_x, m_y)
        tour(m_x, m_y, visitados)
        vistados.remove(m_x, m_y)
    if len(visitados) = 64 and (0,0) in moves
        return true 

```

funcion final

```python
def resolver():
    visitados []
    status = tour(0,0,visitados)
    return status

```


complejidad espacial es de O(n*m)

complejidad temporal O(1)

## ejercicio 10

branch and bound es validar a parte de por estados validos por costos (proyectas costo de una rama y en base a la proyeccion ves si seguis)

n una variante del problema de la mochila, tenemos “n” elementos que podemos
incluir dentro de un contenedor que acepta un total de “K” kilos. Cada elemento tiene un
peso, un valor y un subconjunto de otros elementos con el que es incompatible
seleccionarlo. Debemos seleccionar la combinación de elementos que sume el mayor
valor posible sin incumplir las restricciones. En caso de existir diferentes soluciones
máximas se prefiere a aquella que requiere un menor peso. Resolver por branch and
bound.

armames el arbol en base a si entra un elemento en la mochila o no, lo bueno de armar el arbol en torno a si entra o no es que la cantidad maxima de estados es 2^n (por cada elemenrto la respuesta es si o no)


mochila -> k kilos
n elementos -> pi, vi con p siendo peso y v siendo valor

f costo 

ordenar vi/pi en base a valor maximo por un determinado peso


cortamos por peso libre * vx/px -> ganancia maxina < max_ganancia -> costo

se termina cuando lleguemos a la ultima de las hojas 


```pseudo
- ordenamos los elementos 

    mochila(n, nro_elemento)
        new_m = m union mochila[nro_elemento]
        if nro_elemento != n: -> O(n)
            incomp = incomp(m, nro_elemento)
            supera_peso = new_m.pesos > k
            if mochila[nro_elemento].v/p *(k-m.p) + max_gan > max_gan #fcosto
               if !incomp and !supera_peso:
                  mochila(new_m, nro_elemento + 1)
                mochila(m, nro_elemento + 1)
            else: 
                if !incomp and !supera_peso and new_m.ganancia > max_gan:
                    max_gan = new_mochila.ganancia
                    max_sol = new_mochila
                if m.ganancia > max_gan
                    max_gan = m.ganancia
                    max_sol = m
```

O(2^n*n) -> temporal
O(n) -> espacial

el orden de funcion coste y funcion poda es arbitrario, en branch and bound siempre empieza con el ordenado de los elementos(n log n)


## ejercicio 11

El problema del coloreo de grafos intenta asignar colores a los nodos de un grafo
G=(V,E) de tal forma que dos nodos adyacentes no tengan el mismo color. Un parámetro
de este problema es “c” la cantidad de colores a utilizar. El polinomio cromático es una
función f(G,c) que determina cuántas coloraciones (soluciones al problema de coloreo)
válidas diferentes pueden realizarse en un determinado grafo G utilizando exactamente
“c” colores. Se pide generar mediante backtracking los primeros “c” resultados de f(G,c)
para un determinado grafo G.

G(v,e)

    ```
                (-)
        /   /   \  \
        1   2   3  c
(1,1)   (0,1)

```

O(n^c)

```python

def is_valid(v,c):
    for a in g.ady(v)
        if a < len(solucion)
            if solucion[a] == ci
                return false
            return true
        else:
            return true


```

```python

def coloreos(v,c,solucion):

    soluciones = []
    for i in o...c:
        if not is valid(v,i):
            continue
        solucion.append(i)
        colores(v + 1,c,solucion)
        solucion.pop()
    if solucion = v
        soluciones.append(solucion.copy())


```

complejidad temporal (N^c + 1)
espacial (k*n)