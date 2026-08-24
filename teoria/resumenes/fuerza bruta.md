# fuerza bruta

los algoritmos de fuerza bruta comprenden una familia de algoritmos como busqueda exaustiva, generar y probar, backtracking, branch and bound, etc. donde la principa caracteristica que las une es que dada una instancia del problema, el algoritmo genera todas las posibles soluciones y verifica cual de ellas es la mejor solucion posible.

## casos de uso

1. para probar la correctitud de un algoritmo, es decir, para verificar que el algoritmo produce una solucion correcta para cualquier instancia del problema.

2. cuando el dominio acota a n (es decir el dominio del problema es finito y pequeño), es decir, cuando el algoritmo puede generar todas las posibles soluciones en un tiempo razonable, ejemplo resolver un sudoku, el algoritmo puede generar todas las posibles soluciones en un tiempo razonable.

3. seguridad: se usan para crackear contraseñas, es decir, para generar todas las posibles combinaciones de caracteres y verificar cual de ellas es la correcta.


## espacios canonicos

| Espacio | Cuándo aplica | Problema testigo | Tamaño | Generador | Complejidad total |
|---|---|---|---|---|---|
| **n-tuplas** | elegir un subconjunto cualquiera | Mochila (`§3`) | $2^n$ | contador binario | $O(n2^n)$ |
| **Permutaciones** | ordenar todos los elementos | Viajante (`§4`) | $(n-1)!$ | Narayana Pandita | $O(n!)$ |
| **Combinaciones** | subconjunto de tamaño $k$ **fijo** | Clique (`§5`) | $\binom{n}{k}$ | algoritmo "L" de Knuth | $O\!\left(k^2\binom{n}{k}\right)$ |
| **Particiones** | agrupar sin saber cuántos grupos | Clustering (`§6`) | $B_n$ (Bell) | Hutchinson (RGS) | $O(B_n \cdot f_e(n))$ |
| **Espacio de estados** | secuencia de movimientos/decisiones | 8-puzle (`§7`) | según modelado | DFS / BFS | $O(n+m)$ sobre el grafo |


## componentes de un algoritmo de fuerza bruta

### dominio del problema

son los espacios canonicos que se pueden usar para modelar el problema, es decir, el conjunto de todas las posibles soluciones que se pueden generar, segun la naturaleza del problema es que espacio se va a usar, por ejemplo, si el problema es de combinatoria se puede usar n-tuplas, permutaciones, combinaciones o particiones, si el problema es de busqueda se puede usar un espacio de estados.

### funcion generativa 

recorre todo S produciendo cada candidato c en S, es decir, genera todas las posibles soluciones del problema.

### funcion de prueba

verifica sobre cada candidata las restricciones implicitas del problema, es decir, verifica si la candidata es una solucion valida del problema.

### funcion de evaluacion

asigna un valor a cada candidata, es decir, determina que tan buena es la candidata como solucion del problema.

## backtracking

es un caso particular de fuerza bruta, donde el algoritmo genera todas las posibles soluciones del problema, pero cuando encuentra una candidata que no cumple con las restricciones del problema, descarta esa candidata y no genera todas las posibles soluciones a partir de esa candidata, es decir, poda el espacio de busqueda.

para esto se usa un arbol de soluciones, donde cada nodo del arbol representa una candidata y cada rama representa una decision que se toma para generar nuevas candidatas a partir de la candidata actual, cuando se encuentra una candidata que no cumple con las restricciones del problema, se poda el arbol y no se generan nuevas candidatas a partir de esa candidata.

### funcion de poda

es una funcion que es parte de la funcion de prueba, que verifica si una candidata cumple con las restricciones del problema, si no cumple, se poda el arbol y no se generan nuevas candidatas a partir de esa candidata.

## branch and bound

es una mejora de backtracking, donde a parte de la funcion poda se cuenta en la prueba con la funcion de cota, que permite determinar si una candidata es mejor que la mejor candidata encontrada hasta el momento, si no lo es, se poda el arbol y no se generan nuevas candidatas a partir de esa candidata.
