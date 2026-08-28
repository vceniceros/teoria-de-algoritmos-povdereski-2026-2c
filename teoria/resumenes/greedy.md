# greedy

los algoritmos greedy son una familia de algoritmos que buscan una solucion aproximada a un problema de optimizacion, es decir, buscan una solucion que sea lo suficientemente buena, pero no necesariamente la mejor solucion posible.

se caraterizan por tomar decisiones locales que parecen ser las mejores en ese momento, con la esperanza de que estas decisiones locales conduzcan a una solucion global optima, lo de greedy (avaricioso) es que el algoritmo toma la mejor decision en cada paso, sin considerar las consecuencias futuras de esa decision.

cuando decimos construye es porque greedy va armando la solucion paso a paso mediante los optimos locales, distinto a fuerza bruta que genera todas las posibles soluciones y luego elige la mejor, greedy va construyendo una solucion a partir de decisiones locales.

cuando hablamos de soluciones locales nos referimos a que mientras va iterando sobre el problema, va tomando decisiones que parecen ser las mejores en ese momento, sin considerar las consecuencias futuras de esa decision.

cuando decimos greedy es porque la decision que toma el algoritmo es la que parece ser la mejor en ese momento, sin considerar las consecuencias futuras de esa decision.

## 4 propiedades de un algoritmo greedy

### construccion incremental

la solucion se arma agregando al conjunto solucion un elemento a la vez, es decir, se va construyendo la solucion paso a paso mediante los optimos locales.

### decision irreversible

una vez agregado un elemento al conjunto solucion, no se puede quitar, es decir, la decision que toma el algoritmo es irreversible, distinto a backtracking que puede deshacer decisiones y probar otras alternativas.

### decision local

el criterio se evalua sobre el estado actual, es decir, el algoritmo toma la decision que parece ser la mejor en ese momento, sin considerar las consecuencias futuras de esa decision, esto no significa que no se evaluen estados pasados ya que de hecho la solucion se construye sobre los optimos locales (incluidos los ya seleccionados) si implica que para una solucion local no se analiza el estado futuro (ejemplo: no se podria usar una funcion costo como en branch and bound).

### aplicable a problemas de optimizacion

la unica manera de usarlo para un problema que no es de optimizacion es convirtiendolo en uno, estos algoritmos son aplicables a problemas de optimizacion, es decir, problemas donde se busca maximizar o minimizar una funcion objetivo, por ejemplo, el problema de la mochila, el problema del viajante, el problema de la cobertura de conjuntos, etc.



## Greedy vs. las otras técnicas — tabla de contrastes

## Tabla

| | Fuerza bruta / Generar y probar | Backtracking | Greedy | PD |
|---|---|---|---|---|
| **Cómo explora** | Genera todo el espacio de soluciones candidatas y prueba cada una | Recorre el árbol de soluciones parciales podando ramas inviables | Un solo camino desde la raíz hasta la hoja | Todos los subproblemas, una vez cada uno |
| **¿Deshace?** | No hace falta: no construye, enumera | **Sí** — es su rasgo definitorio | **No, nunca** | No aplica: no hay camino que deshacer |
| **¿Cuándo decide?** | Al final, comparando candidatos completos | Tentativamente, con derecho a revisión | **Antes** de resolver el subproblema | **Después** de resolver los subproblemas |
| **Qué necesita el problema** | Nada. Siempre funciona | Restricciones que permitan podar | Elección greedy + subestructura óptima | Subestructura óptima + subproblemas superpuestos |
| **Costo típico** | Exponencial o factorial | Exponencial en peor caso, práctico con buena poda | Casi siempre $\Theta(n \log n)$, dominado por el orden | Polinomial: subproblemas × opciones |
| **Garantía** | Óptimo siempre | Óptimo siempre | Óptimo **solo si se demuestra** | Óptimo siempre |

## Cómo leerla

**La fila "¿cuándo decide?" es la clave.** Greedy y PD comparten la subestructura
óptima; lo único que los diferencia es el momento de la decisión. En PD la elección
depende de las soluciones de los subproblemas, así que se resuelve bottom-up; en
greedy elegís lo que parece mejor y recién ahí resolvés el subproblema que queda
(`CLRS 15.2`).

**Greedy es backtracking sin backtrack.** Sobre el árbol de decisiones: fuerza bruta
lo recorre entero, backtracking lo recorre podando, greedy baja por una sola rama sin
mirar las hermanas. Por eso es rápido y por eso puede estar mal.


## condiciones de aplicabilidad

a diferencia de otros algortimos en greedy siempre hay que demostrar que la solucion que se obtiene es la mejor posible, lo que limita su aplicabilidad a problemas que cumplan con ciertas condiciones, estas condiciones son:

## elección greedy

se tiene que poder armar una solucion optima global a partir de soluciones optimas locales, es decir, que la solucion optima global se pueda construir a partir de soluciones optimas locales, el teorema principal del que se parte es el siguiente

```math
sea S un subproblema no vacio y sea x el elemento que maximiza el criterio greedy en S, entonces x esta incluido en alguna solucion optima global de S.
```

una eleccion greedy es correcta cuando se cumple que al agarrar ese x, el subproblema que queda (S - {x}) tiene una solucion optima que junto con x forma una solucion optima global de S, es decir, si yo tengo un conjunto S que esta compuesto por soluciones optimas y saco un elemento a y en su lugar pongo mi elemento x, el conjunto resultante sigue siendo optimo, es decir, que la solucion optima global se puede construir a partir de elecciones locales.

## subestructura optima

volviendo a simbolos matematicos

```math
sea S una solucion optima de la instancia P,y sea P′ un subproblema de P.Entonces S ∩ P′ es una solucion optima de P′.
``` 

en criollo si lo saco una solucion del conjunto de solucion global encuentro por definicion la solucion optima del subproblema, es decir, que la solucion optima global contiene soluciones optimas de los subproblemas.

por ejemplo si buscar el camino mas corto entre Retiro y La Plata, y tengo que en este camino tengo que pasar por Quilmes, entonces el tramo Retiro-Quilmes de ese camino tiene que ser el camino mas corto entre Retiro y Quilmes, y el tramo Quilmes-La Plata tiene que ser el camino mas corto entre Quilmes y La Plata, es decir, que la solucion optima global contiene soluciones optimas de los subproblemas.

## que garantiza cada una

|eleccion greedy|subestructura optima|
|---|---|   
|que x es una buena primera decision (esta incluido en alguna solucion optima global)| que resolver el subproblema que queda despues de agarrar x es suficiente para encontrar la solucion optima global|

## como se defina la decision greedy

no hay una forma exacta pero siguiendo los siguientes pasos se puede llegar a una decision greedy correcta:

### enumerar los candidatos

estos son dados por el problema, mirando los datos dados por cada candidato podemos inferir los criterios a tener en cuenta para elegir el candidato que maximiza el criterio greedy.

ejemplo: en el problema del schedualing de la sala de reuniones podemos tener los siguientes candidatos:

```math

r1 = (9:00, 17:00)
r2 = (10:00, 11:00)
r3 = (12:00, 14:00)
r4 = (13:00, 13;30)

```

a partir de aca puedo elaborar 3 criterios para elegir el candidato que maximiza el criterio greedy:

1. elegir la reunion que empieza mas temprano
2. elegir la reunion mas corta
3. elegir la reunion que termina mas temprano

### intentar romper los criterios seleccionados

en greedy es mas facil demostrar que un criterio esta mal que demostrar que esta bien, por lo tanto es recomendable intentar romper los criterios seleccionados para ver si alguno de ellos no es correcto.

ejemplo:

1. elegir la reunion que empieza mas temprano: si elijo r1, no puedo elegir ninguna otra reunion porque esta ocupa todo el dia la sala
2. si elijo la mas corta, puedo elegir r2 y r4, pero no puedo elegir r3, por lo tanto no es optimo
3. si elijo la que termina mas temprano, puedo elegir r2 y r3, por lo tanto es optimo, y tiene cara de ser el criterio correcto, pero hay que demostrarlo.


### valida que tenga sentido

el criterio que sobrevivio, tiene una explicacion semantica, es decir, tiene sentido, por ejemplo en el caso de las reuniones, elegir la que termina mas temprano tiene sentido porque me deja mas tiempo para elegir otras reuniones, casi siempre la pregunta que hay que responder es " cual es el recurso mas escaso que estoy tratando de optimizar?" y el criterio greedy tiene que estar relacionado con ese recurso escaso.
para este caso el recurso escaso es el tiempo de la sala de reuniones, y el criterio greedy esta relacionado con optimizar ese recurso escaso.

### demostrar que es correcto

para esto podemos probar casos bordes y si ninguno rompe el criterio entonces podemos demostrar que es correcto, los tipicos casos bordes son:

1. un solo candidato grande vs muchos candidatos chicos: si elijo el candidato grande, no puedo elegir ninguno de los chicos, por lo tanto no es optimo, si elijo los chicos, puedo elegir todos los chicos y es optimo, por lo tanto el criterio greedy es correcto.

2. un solo candidato parece bueno pero bloquea a 2 candidatos chicos: si elijo el candidato grande, no puedo elegir ninguno de los chicos, por lo tanto no es optimo, si elijo los chicos, puedo elegir ambos y es optimo, por lo tanto el criterio greedy es correcto.

3. un candidato que desperdicia recursos: si elijo el candidato grande, no puedo elegir ninguno de los chicos, por lo tanto no es optimo, si elijo los chicos, puedo elegir ambos y es optimo, por lo tanto el criterio greedy es correcto.


## probar que greedy es optimo

aca viene la verdadera complejidad de greedy, demostrar que es optimo, para esto tenemos dos tecnicas ideales

### greedy por delante

comparas tu solucion contra una optima, elemento por elemento en la misma
posicion, y mostras que la tuya nunca va atras SEGUN EL CRITERIO.

ejemplo (reuniones, criterio = termina primero):
tu 1ra reunion termina antes o igual que la 1ra del optimo.
tu 2da termina antes o igual que la 2da del optimo. y asi.
formal: f(i_r) <= f(j_r) para todo r  (KT 4.1)

por que se cumple: si venis adelante, tu sala se libero antes, asi que todo
lo que el optimo puede elegir vos tambien lo podes elegir. y tu criterio
agarra la que termina antes de las disponibles.

cierre: si el optimo tuviera MAS elementos, tendria uno despues del ultimo
tuyo — pero ese tambien te servia a vos y lo habrias agarrado.

sirve cuando el objetivo es CONTAR cosas.

### intercambio de elementos

no comparas: TRANSFORMAS. agarras una solucion optima y la vas modificando
de a un paso, sin que empeore nunca, hasta que tiene la forma de la tuya.
si nunca empeoro y termino siendo la tuya, la tuya ya era optima.

ejemplo (trabajos con deadline, criterio = EDF):
- inversion = un trabajo que vence despues puesto antes que uno que vence antes
- mi solucion no tiene inversiones (ordene por deadline, sale gratis)
- si el optimo tiene una inversion, tiene dos trabajos PEGADOS dados vuelta
- los permuto entre si (mismos elementos, cambia el orden)
- pruebo que ese swap NO EMPEORA el atraso maximo
- repito hasta que no queden inversiones -> quedo con la forma de la mia

ojo: en cada paso se prueba "no empeora", no "sigue siendo optimo".
lo segundo se DEDUCE de lo primero.

ojo 2: los dos elementos tienen que estar PEGADOS. si agarras dos al azar
se te mueve todo lo del medio y la cuenta no cierra.

sirve cuando importa el ORDEN, o cuando stays ahead no arranca.

## Catálogo de problemas greedy


## Tabla principal

| Problema | Objetivo | Decisión greedy | Prueba | Complejidad | Fuente |
|---|---|---|---|---|---|
| **Interval Scheduling** | Máxima cantidad de intervalos compatibles | El de menor $f(i)$ (termina antes) | Stays ahead | $\Theta(n\log n)$ | `KT 4.1` |
| **Interval Partitioning** | Mínima cantidad de recursos para meter todos | Ordenar por $s(i)$ y asignar cualquier etiqueta libre | Alcanza la cota inferior (profundidad) | $\Theta(n\log n)$ | `KT 4.1` |
| **Minimize Lateness** | Minimizar el atraso máximo | EDF: menor deadline $d_i$ | Intercambio (inversiones) | $\Theta(n\log n)$ | `KT 4.2` |
| **Caching óptimo** † | Minimizar cache misses (offline) | Desalojar el bloque de uso más lejano en el futuro | Intercambio | — | `KT 4.3`, `CLRS 15.4` |
| **Camino mínimo (Dijkstra)** | Distancias mínimas desde $s$ | El nodo $v \notin S$ que minimiza $d(u) + \ell_e$ | Stays ahead | $O(m\log n)$ con heap | `KT 4.4` |
| **MST — Kruskal** | Árbol generador de costo mínimo | La arista más barata que no cierre ciclo | Cut Property | $O(m\log n)$ | `KT 4.5`, `4.6` |
| **MST — Prim** | Ídem | La arista más barata que conecta $S$ con $V-S$ | Cut Property | $O(m\log n)$ | `KT 4.5`, `4.6` |
| **MST — Reverse-Delete** | Ídem | Borrar la más cara que no desconecte | Cycle Property | Difícil de acotar bien | `KT 4.5` |
| **Clustering de máximo espaciado** † | Maximizar la distancia mínima entre clusters | Kruskal frenado al llegar a $k$ componentes | Argumento directo vía MST | $O(m\log n)$ | `KT 4.7` |
| **Códigos de Huffman** | Código libre de prefijos de costo mínimo | Fusionar los dos de menor frecuencia | Elección greedy + subestructura | $O(n\log n)$ | `KT 4.8`, `CLRS 15.3` |
| **Mochila fraccionaria** | Maximizar valor con peso $\le W$ | Mayor ratio $v_i/w_i$ | Elección greedy | $O(n\log n)$ | `CLRS 15.2` |

## Qué recurso optimiza cada criterio

Sirve para el paso "¿qué es lo escaso?" cuando el ejercicio no es ninguno de estos.

| Problema | Recurso escaso | Por qué ese criterio lo cuida |
|---|---|---|
| Interval Scheduling | La línea de tiempo | Terminar antes libera el recurso para la mayor cantidad de pedidos siguientes (`CLRS 15.1`) |
| Interval Partitioning | Cantidad de recursos | Barrer de izquierda a derecha nunca necesita más etiquetas que la profundidad |
| Minimize Lateness | Tiempo antes de cada vencimiento | La presión viene de los deadlines, no de las duraciones |
| Caching | Los $k$ slots | Sacar lo que menos falta hace pospone el próximo miss |
| Dijkstra | — (costo acumulado) | El nodo más cercano ya no puede mejorarse con aristas no negativas |
| MST | — (costo total) | Cut Property: la más barata que cruza un corte está en todo MST |
| Mochila fraccionaria | El peso | Máximo pago por unidad de recurso consumido |

## Notas por problema

**Interval Scheduling** — Los tres criterios descartados: menor $s(i)$, menor
$f(i)-s(i)$, y menos conflictos (`KT 4.1`). Tenerlos a mano: son la respuesta a
"¿por qué este criterio y no otro?".

**Interval Partitioning** — La prueba es distinta de las otras dos técnicas: se
define la *profundidad* $d$ (máxima cantidad de intervalos que se solapan en un
punto), se observa que $d$ es cota inferior de recursos necesarios, y se muestra que
el algoritmo usa exactamente $d$ (`KT 4.1`).

**Minimize Lateness** — Criterio descartado: menor holgura $d_i - t_i$.
Contraejemplo de dos trabajos: $t_1=1, d_1=2$ y $t_2=10, d_2=10$ (`KT 4.2`).
La prueba encadena tres pasos: existe un óptimo sin tiempo ocioso → existe uno sin
inversiones → todos los sin-inversiones tienen el mismo atraso máximo.

**Dijkstra** — Es stays ahead, no intercambio: se prueba inductivamente que cada vez
que se selecciona un camino a $v$, ese camino es más corto que cualquier otro
posible a $v$ (`KT 4.4`). **Requiere aristas no negativas.** Con costos negativos
falla, y sumar una constante a todas las aristas tampoco arregla nada porque cambia
la identidad del camino mínimo (`KT 6.8`).

**MST** — La prueba no es sobre los algoritmos sino sobre dos propiedades del grafo:

- **Cut Property**: para todo corte $S$, la arista más barata que cruza de $S$ a
  $V-S$ pertenece a **todo** MST. Kruskal y Prim son óptimos porque solo agregan
  aristas justificadas por ella (`KT 4.5`).
- **Cycle Property**: en todo ciclo $C$, la arista más cara **no** pertenece a
  ningún MST. Justifica Reverse-Delete (`KT 4.5`).

Ambas asumen **costos distintos**. Si hay empates se perturban los costos, y todo MST
de la instancia perturbada también lo es de la original (`KT 4.5`).

**Clustering** — Es Kruskal con un criterio de parada: se corta al quedar $k$
componentes. Equivale a construir el MST completo y borrarle las $k-1$ aristas más
caras (`KT 4.7`). El espaciado resultante es exactamente la longitud de la arista que
Kruskal habría agregado a continuación.

**Huffman** — El greedy no construye la solución directamente: **achica la instancia**.
Fusiona los dos símbolos de menor frecuencia en uno solo cuya frecuencia es la suma, y
resuelve recursivamente el problema con un símbolo menos (`KT 4.8`). Implementación con
min-priority queue: $n-1$ fusiones, cada una con dos `EXTRACT-MIN` y un `INSERT`
(`CLRS 15.3`).

**Mochila fraccionaria** — Es el contraste obligatorio con la 0-1. Ambas tienen
subestructura óptima; solo la fraccionaria tiene la propiedad de elección greedy
(`CLRS 15.2`). Ver la sección "dónde se rompe".

## Cómo usar esta tabla en el parcial

1. Leé el enunciado y buscá a cuál de estos se parece. Cubre la mayoría de los casos.
2. Si es una variante, chequeá **qué cambió**: ¿agregaron pesos? ¿los objetos dejaron
   de ser divisibles? ¿hay tiempos de liberación?
3. Los cambios que suelen romper el greedy:
   - agregar **valores/pesos** a los ítems → Weighted Interval Scheduling, va PD (`KT 6.1`)
   - hacer los objetos **indivisibles** → mochila 0-1, va PD (`CLRS 15.2`)
   - agregar **release times** a los trabajos → el problema se vuelve mucho más
     difícil de resolver óptimamente (`KT 4.2`)
   - permitir **costos negativos** en las aristas → Dijkstra falla, va PD (`KT 6.8`)

## hoja de chequeo

cuando te enfrentes a un problema nuevo, seguí estos pasos para ver si es greedy:

## Diagnóstico: ¿es greedy este ejercicio?

1. **¿Es un problema de optimización?** (hay un máx/mín) → si no, greedy no aplica.
2. **¿Se parece a alguno del catálogo?** → usá ese criterio y adaptalo. Cubre la mayoría.
3. **¿Tiene subestructura óptima?** → probala con cut-and-paste. Si no la hay, ni greedy ni PD.
4. **¿Puedo decidir sin resolver los subproblemas?**
   - Sí → **greedy**
   - No, necesito comparar incluir-vs-excluir → **PD**
5. **¿Los objetos son divisibles?** → la indivisibilidad es lo que más rompe greedy.

## Buscar el criterio

1. Listá los candidatos que salen de los datos de cada objeto (son 3 o 4).
2. Intentá **romper** cada uno con un ejemplo de 3 elementos. Es mucho más barato que probar.
3. Chequeá el sobreviviente contra: **¿qué es lo escaso, y qué elección lo cuida?**
4. Si los rompés a todos → **eso también es una respuesta**: el problema va por PD.

**Dónde está el contraejemplo** (casi siempre en uno de estos tres moldes):

- uno enorme contra varios chicos
- uno que solo parece bueno pero bloquea a dos
- uno que deja el recurso parcialmente desperdiciado

## Demostrar

| Técnica | Qué hacés | Cuándo |
|---|---|---|
| **Stays ahead** | Comparás elemento por elemento, misma posición, y mostrás que nunca vas atrás según el criterio | El objetivo es **contar** cosas |
| **Intercambio** | Transformás un óptimo en tu solución, paso a paso, sin que empeore nunca | Importa el **orden**, o stays ahead no arranca |

**Plantilla de CLRS** (`CLRS 15.2`), sirve para cualquiera de las dos:

1. Plantear el problema como "hago una elección y me queda **un** subproblema".
2. Probar que **existe algún óptimo que incluye mi elección** (elección segura).
3. Mostrar que **mi elección + el óptimo de lo que quedó = óptimo del original**.

Se prueba **una sola vez**, no por iteración: lo que queda es el mismo problema más
chico, y el argumento se reaplica por inducción.

## Errores que se cobran

- ❌ **"Probé con estos ejemplos y anduvo"** → no es demostración. Un contraejemplo
  rompe un criterio; mil ejemplos buenos no lo salvan.
- ❌ **"Mi elección está en todas las soluciones óptimas"** → falso casi siempre.
  Es en **alguna**.
- ❌ **Intercambiar dos elementos cualesquiera** → tienen que estar **pegados** y
  formar una inversión. Si no, se te mueve todo lo del medio.
- ❌ **"El óptimo global se arma con óptimos locales"** → *óptimo local* es de
  búsqueda local (`AP-MH`). Se dice **elecciones localmente óptimas**.
- ❌ **Escribir $O$ donde va $\Theta$.** Si el orden domina y conocés el
  comportamiento exacto, es $\Theta(n\log n)$.
- ❌ **Olvidar el preprocesamiento en la complejidad.** El barrido es $\Theta(n)$,
  pero ordenar cuesta $O(n\log n)$ y hay que sumarlo.
- ❌ **Definir el subproblema como $S - \{x\}$.** Es "lo que sigue siendo compatible
  con $x$", que puede sacar muchos más elementos.

## Si el greedy no cierra

No es una derrota. Escribir *"los criterios naturales A, B y C fallan por estos
contraejemplos, por eso el problema requiere PD"* es una respuesta completa.

Es exactamente lo que hace `KT 6.1` con Weighted Interval Scheduling: al agregar
valores a los intervalos, ni siquiera el criterio que funcionaba antes sigue siendo
óptimo, y no se conoce ningún greedy natural. Eso es lo que motiva el cambio de técnica.

## Frases para tener a mano

- Un algoritmo es greedy si construye una solución en pasos chicos, eligiendo en cada
  paso de manera miope para optimizar algún criterio subyacente (`KT 4`).
- Inventar un greedy es fácil; encontrar los casos en que funciona y **probar** que
  funciona es el desafío interesante (`KT 4`).
- Debajo de casi todo algoritmo greedy hay una solución de PD más engorrosa (`CLRS 15.2`).
- Greedy elige **antes** de resolver los subproblemas; PD resuelve **antes** de elegir
  (`CLRS 15.2`).