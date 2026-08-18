# introduccion a teoria de algoritmos

en la materia se resuelven problemas de indole computacional

## problemas

cosas que queremos resolver, se dividen en instacias y soluciones

### instancia

es un conjunto particular de datos que representa un problema, por ejemplo, una lista de numeros enteros.

### solucion

es un conjunto de datos que representa la respuesta a un problema, por ejemplo, la lista de numeros enteros ordenada.

se puede dar que varias instancias tengan la misma solucion, que sea 1 a 1, o que varias instancias tengan varias soluciones, que sea 1 a n.

### tipos de problemas

segun el tipo de problema que tengamos va a ser el tipo de solucion que vamos a dar, entonces tenemos los siguientes tipos de problemas:

#### optimizacion

en general buscan maximizar o minimizar algo en funcion de una instancia, por ejemplo, el problema del viajante de comercio busca minimizar la distancia recorrida para visitar un conjunto de ciudades, para esta instancia de problema la solucion seria dada por que pasos seguir para alcanza la optimalidad, en este caso seria que ciudades visitar y en que orden.

#### evaluacion

es un problema que busca determinar si una instancia cumple con ciertas condiciones, seria de una determinada instancia quedarte solamente con el resultado especifico de la solucion y ver si este cumple con las condiciones, para el problema del viajante de comercio seria quedarse solamente con la distancia recorrida y ver si esta es menor a un valor dado.

#### decision

son problemas booleanos, es decir, que la solucion es un si o un no, por ejemplo, el problema del viajante de comercio seria determinar si existe un camino que recorra todas las ciudades y que la distancia recorrida sea menor a un valor dado.

#### localizacion (buscar)

son problemas que buscan encontrar un elemento dentro de un conjunto de elementos, por ejemplo, buscar un numero en una lista de numeros enteros, en este caso se busca una instancia que cumpla con ciertas condiciones, por ejemplo, que el numero buscado sea igual a un valor dado.

#### enumeracion combinatoria

son problemas que buscan encontrar todas las soluciones posibles para una instancia dada, en el ejemplo del viajante de comercio seria encontrar todos los caminos posibles que recorran todas las ciudades y determinar cual es el camino mas corto.


## antipatron del martillo de maslow    

es tentador pensar que si la herramienta que tenemos es un martillo, entonces todos los problemas son clavos, basicamente seria para todos los tipos de problemas usar la misma solucion.

## algoritmos

es un conjunto de instrucciones que permite a una instancia de un problema llevar a una solucion, es decir, es un conjunto de pasos que nos permite resolver un problema.

## definicion de D. Knuth

es un conjunto finito de reglas que da una secuencia de operaciones para resolver un problema especifico, debe cumplir 5 requisitos:

1. debe ser finito, es decir, que tenga un numero finito de pasos.
2. debe ser preciso, es decir, que cada paso este claramente definido.
3. entrada: debe recibir un conjunto de valores antes de iniciar
4. salida: debe producir un conjunto de valores al finalizar que estan relacionados con la entrada.
5. eficiencia: debe poder concretarse en un tiempo finito y las operacines deben ser tan simples como para ser ejecutadas por una persona con lapiz y papel.

la palabra algoritmo viene del matematico Mohammad ibn Musa al-Khwarizmi, quien escribio un libro sobre algebra y aritmetica en el siglo IX, y su nombre fue latinizado como Algoritmi, introduce el sistema numerico hindu-árabe y el concepto de algoritmo, que es un conjunto de reglas para resolver problemas matemáticos.

## Analisis de algoritmos

a la hora de analizar un algoritmo son varios los aspectos que se deben tener en cuenta, entre ellos:

### problema 

el problema que se quiere resolver, es decir, la instancia y la solucion que se busca.

### solucion algoritmica

es el conjunto de pasos que se deben seguir para resolver el problema, es decir, el algoritmo en si.

### complejidad de algoritmos

es el estudio de los recursos que requiere un algoritmo para resolver un problema, es decir, el tiempo y el espacio que requiere para ejecutarse.

### optimalidad y margen de error

es decir , si el algoritmo es capaz de encontrar la mejor solucion posible para un problema, o si existe un margen de error en la solucion que se obtiene.

### caracteristicas de la solucion

a veces se olvida pero es importante ver las formas en que se puede representar la solucion.


## complejidad computacional

es el estudio de los recursos que requiere un algoritmo para resolver un problema, es decir, el tiempo y el espacio que requiere para ejecutarse.

no intersa ver para una funcion g(n) siendo g el algoritmo y n la instancia del problema, para cuanto cresca n cuanto crece g(n), es decir, cuanto tiempo y espacio requiere el algoritmo para resolver el problema.

### omega

es el limite inferior de la complejidad de un algoritmo, es decir, el tiempo minimo que requiere para resolver un problema(nunca se comporta peor que).

### O

es el limite superior de la complejidad de un algoritmo, es decir, el tiempo maximo que requiere para resolver un problema(siempre se comporta peor que).

### Theta

es el limite exacto de la complejidad de un algoritmo, es decir, el tiempo exacto que requiere para resolver un problema(siempre se encuentra entre una funcion y otra).


## como analizar un algoritmo

en base a como se comporta segun la instancia analizando distintos casos puntuales:

mejor caso: es el caso en el que el algoritmo se comporta de la mejor manera posible, es decir, requiere el menor tiempo y espacio posible para resolver un problema.

peor caso: es el caso en el que el algoritmo se comporta de la peor manera posible, es decir, requiere el mayor tiempo y espacio posible para resolver un problema.

caso promedio: es el caso en el que el algoritmo se comporta de manera promedio, es decir, requiere un tiempo y espacio promedio para resolver un problema.

para analizar correctamente un algoritmo se debe analizar el peor caso, en el ejemplo del viajante de comercio, el peor caso seria que el algoritmo recorra todas las ciudades y que la distancia recorrida sea mayor a un valor dado.

## correctitud y optimalidad

un algoritmo es correcto si para cualquier instancia del problema, el algoritmo produce una solucion que cumple con las condiciones del problema, es decir, que la solucion es correcta, basta encontrar una instancia para la cual el algoritmo no produce una solucion correcta para decir que el algoritmo es incorrecto, tambien para cualquier instancia el algortimo debe producir una solucion en un tiempo finito.

por otro lado un algoritmo es optimo si para cualquier instancia del problema, el algoritmo produce una solucion que es la mejor posible, es decir, que no existe otra solucion mejor para esa instancia del problema y tambien finaliza en un tiempo finito.

## demostracion de correctitud y optimalidad

utilizamos razonamiento matematico para demostrar que un algoritmo es correcto y optimo, es decir, que para cualquier instancia del problema, el algoritmo produce una solucion correcta y optima, algunas tencicas que se utilizan son:

- por definicion
- por casos
- por induccion
- por contrareciproco
- por absurdo
- por contraejemplo