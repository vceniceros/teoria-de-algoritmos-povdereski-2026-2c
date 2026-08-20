# apuntes fuerza bruta

son soluciones que buscan todas las posibles soluciones de un problema y eligen la mejor. Son soluciones que no son eficientes, pero son fáciles de implementar y entender, para una instancia dada a a buscar *TODOS* los conjuntos soluciones posibles y elegir la mejor.

## es valido?

recontra, siempre va a ser valido porque busca todas las posibles soluciones, por lo que si existe una solución, la va a encontrar.

## es optimo?

probablemente no, crece en el mejor de los casos de forma lineal (en el peor de los casos crece de forma exponencial), por lo que no es optimo.

## problemas donde se puede aplicar

### problema de la mochila

tengo una mochila con un peso máximo y tengo una serie de objetos con un peso y un valor(ese valor puede ser capacidad de supervivencia, precio para una venta, etc). El objetivo es meter en la mochila los objetos que maximicen el valor total sin superar el peso máximo.

asumimos que los elementos son indivisibles, es decir, no podemos meter la mitad de un objeto en la mochila, no son repetibles, es decir, no podemos meter el mismo objeto dos veces en la mochila y que el peso máximo de la mochila es un número entero, no importa el orden en el que se meten los objetos. 

el espacion de solucion es de 2^n, donde n es la cantidad de objetos que tenemos. Esto se debe a que para cada objeto podemos decidir si lo metemos o no en la mochila, por lo que para cada objeto tenemos dos posibilidades.

### el 8 puzzle 

en un tablero de 3x3 tenemos 8 fichas numeradas del 1 al 8 y un espacio vacío. El objetivo es mover las fichas para que queden en orden, es decir, que la ficha 1 esté en la posición (0,0), la ficha 2 en la posición (0,1), la ficha 3 en la posición (0,2), la ficha 4 en la posición (1,0), la ficha 5 en la posición (1,1), la ficha 6 en la posición (1,2), la ficha 7 en la posición (2,0) y la ficha 8 en la posición (2,1).

### n reinas

tenemos un tablero de ajedrez de n x n y queremos colocar n reinas en el tablero de tal manera que ninguna reina ataque a otra. Una reina puede atacar a otra si están en la misma fila, columna o diagonal, cada celda es un elemento, se lo puede representar con un vector de n elementos.


como se puede observar, la fuerza bruta es una técnica que puede ser aplicada a muchos problemas, al fin y al cabo para todos estos ejemplos la fuerza bruta puede buscar todos los conjuntos posibles de soluciones y elegir la mejor. Sin embargo, como se mencionó anteriormente, la fuerza bruta no es eficiente y puede ser muy lenta para problemas grandes, por lo que en la práctica se suelen utilizar otras técnicas más eficientes para resolver estos problemas, en el ejemplo de n reinas vas a tener que buscar entre n! posibles soluciones, lo cual es muy grande para n grande. 


### problema del viajante de comercio

tenemos n ciudades a visitar, cada camino entre dos ciudades tiene un costo asociado, el objetivo es encontrar el camino más corto que pase por todas las ciudades exactamente una vez y regrese a la ciudad de origen. El espacio de soluciones es de (n-1)!/2, ya que para n ciudades hay (n-1)! formas de ordenarlas y como el camino es cíclico, se divide entre 2.

## procedimiento de resolución

podemos pensar como una serie de decisiones sobre las instancias del problema que modifica su estado,un nuevo estado me puede llevar a nuevos estados y así sucesivamente hasta que lleguemos a un estado final, que es aquel que cumple con las condiciones del problema.

## grafo de estados

es un grafo donde cada nodo representa un estado del problema y cada arista representa una decisión que nos lleva a un nuevo estado. El objetivo es encontrar un camino desde el estado inicial hasta un estado final que cumpla con las condiciones del problema.

## ejemplo de la mochila

### estado inicial 

mochila vacia

### transiciones

ir agregando objetos a la mochila o sacando objetos de la mochila.

### estado final

es aquel que cumple con las condiciones del problema, es decir, que el peso total de los objetos en la mochila no supere el peso máximo y que el valor total de los objetos en la mochila sea el máximo posible.

## algunos metodos

- busqueda por anchura

- busqueda por profundidad

- busqueda por profundidad limitada

- generar y probar

- branch and bound

- backtracking


## generar y probar

tenemos una funcion generativa y otra funcion de prueba, la funcion generativa genera todas las posibles soluciones y la funcion de prueba verifica si una solucion es valida o no. Si una solucion es valida, se guarda como la mejor solucion encontrada hasta el momento. Al final, se devuelve la mejor solucion encontrada.

## generar

debe generar todas las posibles soluciones del problema, es decir, debe constar con

1. una estructura de datos que represente el estado del problema, por ejemplo, un vector de n elementos para el problema de n reinas.

2. una manera de obtener la siguiente solucion a partir de la solucion actual.

3. una manera de verificar que no quedan mas soluciones por generar, es decir, que se han generado todas las posibles soluciones.

## probar

debe verificar si una solucion es valida o no, es decir, si cumple con las condiciones del problema. Por ejemplo, en el problema de n reinas, una solucion es valida si ninguna reina ataca a otra, consta de:

1. una manera de verificar si una solucion es valida o no, es decir, si cumple con las condiciones del problema.

2. una manera de guardar la mejor solucion encontrada hasta el momento, es decir, aquella que cumple con las condiciones del problema y tiene el valor maximo.

una solucion factible es aquella que cumple con las condiciones del problema, es decir, que el peso total de los objetos en la mochila no supere el peso máximo y que el valor total de los objetos en la mochila sea el máximo posible.

una solucion optima es aquella que cumple con las condiciones del problema y tiene el valor maximo, es decir, que no existe otra solucion factible que tenga un valor mayor.

casi siempre se usa un vector y un contador binario para generar todas las posibles soluciones, el vector representa el estado del problema y el contador binario representa la solucion actual. Por ejemplo, en el problema de n reinas, el vector representa el tablero de ajedrez y el contador binario representa la posicion de las reinas en el tablero.

### complejidades 

complejidad temporal: O(n2^n), donde n es la cantidad de elementos del problema, ya que para cada elemento se generan 2 posibles soluciones y se verifica si cada solucion es valida o no.

## backtracking

es generar y probar pero con poda, es decir, que si en algun momento se encuentra una solucion que no es valida, se descarta y no se generan mas soluciones a partir de esa solucion. Esto permite reducir el espacio de soluciones y mejorar la eficiencia del algoritmo.

se va poblando el grafo de estados y se va verificando si cada estado es valido o no, si un estado no es valido, se descarta y no se generan mas estados a partir de ese estado. Esto permite reducir el espacio de soluciones y mejorar la eficiencia del algoritmo.

### propiedad de corte

basicamente es una manera de podar el grafo de estados, es decir, de descartar aquellos estados que no pueden llevar a una solucion valida, se empieza a bajar por una hoja (estado) y se va verificando si es valido o no, si no es valido, se descarta y no se generan mas estados a partir de ese estado. Esto permite reducir el espacio de soluciones y mejorar la eficiencia del algoritmo.


en el peor escenario (no se puede podar porque todas las soluciones son validas) la complejidad temporal es O(n2^n), donde n es la cantidad de elementos del problema, ya que para cada elemento se generan 2 posibles soluciones y se verifica si cada solucion es valida o no.

## branch and bound

es una variante de backtracking, pero pensado para optimizar, es decir, se agrega una funcion de cota que permite descartar aquellos estados que no pueden llevar a una solucion optima, se empieza a bajar por una hoja (estado) y se va verificando si es valido o no, si no es valido, se descarta y no se generan mas estados a partir de ese estado. Esto permite reducir el espacio de soluciones y mejorar la eficiencia del algoritmo.

### funcion de cota

va proyectando el valor de la solucion actual y comparandolo con el valor de la mejor solucion encontrada hasta el momento, si el valor de la solucion actual es menor que el valor de la mejor solucion encontrada hasta el momento, se descarta y no se generan mas estados a partir de ese estado. Esto permite reducir el espacio de soluciones y mejorar la eficiencia del algoritmo., aca en vez de dfs para recorrer el grafo de estados se puede usar dfsbb, bfs y dfsbb con sussesor ordering, que es una manera de ordenar los sucesores de un estado de manera que se generen primero aquellos estados que tienen mayor probabilidad de llevar a una solucion optima.

para optimizacion, branch and bound es mejor que backtracking, ya que permite descartar aquellos estados que no pueden llevar a una solucion optima, dando complejidad temporal de O(n2^n) en el peor escenario pero en el mejor escenario puede llegar a ser O(nlogn), donde n es la cantidad de elementos del problema, ya que para cada elemento se generan 2 posibles soluciones y se verifica si cada solucion es valida o no.