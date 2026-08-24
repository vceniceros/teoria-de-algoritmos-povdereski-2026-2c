import unittest

# Problema: 3 caníbales y 3 vegetarianos deben cruzar un río en un bote
# que soporta hasta 2 personas. Si en alguna orilla hay vegetarianos y
# estos son menos que los caníbales presentes en esa misma orilla, son
# atacados. El bote no puede cruzar vacío (alguien tiene que remarlo).
#
# Estado = (caníbales en la orilla izquierda, vegetarianos en la orilla
# izquierda, lado en el que se encuentra el bote). Las cantidades de la
# orilla derecha se derivan como el complemento respecto del total.

TOTAL_CANIBALES = 3
TOTAL_VEGETARIANOS = 3
CAPACIDAD_BOTE = 2

ESTADO_INICIAL = (TOTAL_CANIBALES, TOTAL_VEGETARIANOS, "izquierda")
ESTADO_FINAL = (0, 0, "derecha")


def generar_orillas(estado):
    """Función generar: dado un estado, produce todas las orillas
    (nuevos estados) alcanzables moviendo el bote una vez, con entre 1 y
    CAPACIDAD_BOTE personas, tomadas del lado donde el bote se encuentra."""
    c_izq, v_izq, lado = estado
    if lado == "izquierda":
        disponibles_c, disponibles_v = c_izq, v_izq
    else:
        disponibles_c, disponibles_v = TOTAL_CANIBALES - c_izq, TOTAL_VEGETARIANOS - v_izq

    orillas = []
    for c_bote in range(0, min(CAPACIDAD_BOTE, disponibles_c) + 1):
        for v_bote in range(0, min(CAPACIDAD_BOTE, disponibles_v) + 1):
            personas_en_bote = c_bote + v_bote
            if 1 <= personas_en_bote <= CAPACIDAD_BOTE:
                if lado == "izquierda":
                    nuevo_estado = (c_izq - c_bote, v_izq - v_bote, "derecha")
                else:
                    nuevo_estado = (c_izq + c_bote, v_izq + v_bote, "izquierda")
                orillas.append(nuevo_estado)
    return orillas


def poda(estado):
    """Descarta un estado si en alguna orilla hay vegetarianos en
    minoría frente a los caníbales (habiendo al menos un vegetariano,
    ya que sin vegetarianos presentes no hay a quien atacar)."""
    c_izq, v_izq, _ = estado
    c_der, v_der = TOTAL_CANIBALES - c_izq, TOTAL_VEGETARIANOS - v_izq
    peligro_izq = 0 < v_izq < c_izq
    peligro_der = 0 < v_der < c_der
    return peligro_izq or peligro_der


def prueba(estado, visitados, camino):
    """Función de prueba: arma el árbol de potenciales soluciones
    explorando por backtracking el espacio de estados. Cada rama
    representa un cruce del bote; si el estado resultante está podado
    o ya fue visitado en el camino actual, se descarta esa rama."""
    camino.append(estado)

    if estado == ESTADO_FINAL:
        return True

    visitados.add(estado)
    for siguiente in generar_orillas(estado):
        if siguiente in visitados or poda(siguiente):
            continue
        if prueba(siguiente, visitados, camino):
            return True
    visitados.discard(estado)

    camino.pop()
    return False


def resolver():
    """Punto de entrada: intenta encontrar una secuencia de cruces
    válida desde el estado inicial hasta el estado final."""
    camino = []
    if prueba(ESTADO_INICIAL, set(), camino):
        return camino
    return None

#--------------------#
# complejidad espacial: O(n²) porque para cada estado se guarda en el conjunto de visitados y en el camino, y hay O(n²) estados posibles ((n+1)² combinaciones de orilla por 2 posiciones del bote).
# complejidad temporal: O(n²) porque en el peor caso se exploran todos los estados posibles


class TestCrucePeligroso(unittest.TestCase):

    def test_generar_orillas_desde_estado_inicial(self):
        orillas = generar_orillas(ESTADO_INICIAL)
        # con 3 caníbales y 3 vegetarianos del lado izquierdo, cruzar 2
        # caníbales es una de las jugadas posibles
        self.assertIn((1, 3, "derecha"), orillas)
        # cruzar 1 caníbal y 1 vegetariano también es válido como movimiento
        self.assertIn((2, 2, "derecha"), orillas)
        # el bote nunca puede quedar vacío ni exceder su capacidad
        for c_izq, v_izq, _ in orillas:
            personas_cruzadas = (TOTAL_CANIBALES - c_izq) + (TOTAL_VEGETARIANOS - v_izq)
            self.assertTrue(1 <= personas_cruzadas <= CAPACIDAD_BOTE)

    def test_generar_orillas_no_supera_capacidad_bote(self):
        estado = (0, 0, "derecha")  # bote del lado derecho con las 6 personas
        orillas = generar_orillas(estado)
        for c_izq, v_izq, lado in orillas:
            self.assertEqual(lado, "izquierda")
            self.assertTrue(1 <= c_izq + v_izq <= CAPACIDAD_BOTE)

    def test_poda_detecta_situacion_de_peligro(self):
        # 2 caníbales y 1 vegetariano en la izquierda: el vegetariano es atacado
        self.assertTrue(poda((2, 1, "izquierda")))
        # equivalente pero el peligro está del lado derecho (2 caníbales, 1 vegetariano)
        self.assertTrue(poda((1, 2, "derecha")))

    def test_poda_permite_estados_seguros(self):
        # sin vegetarianos presentes en la orilla no hay riesgo, aunque haya caníbales
        self.assertFalse(poda((2, 0, "izquierda")))
        # misma cantidad de vegetarianos que de caníbales es seguro
        self.assertFalse(poda((1, 1, "izquierda")))
        # el estado inicial y el final son seguros por definición
        self.assertFalse(poda(ESTADO_INICIAL))
        self.assertFalse(poda(ESTADO_FINAL))

    def test_resolver_encuentra_solucion(self):
        camino = resolver()
        self.assertIsNotNone(camino)
        self.assertEqual(camino[0], ESTADO_INICIAL)
        self.assertEqual(camino[-1], ESTADO_FINAL)

    def test_solucion_respeta_todas_las_restricciones(self):
        camino = resolver()
        self.assertIsNotNone(camino)
        for estado in camino:
            self.assertFalse(poda(estado))
        for actual, siguiente in zip(camino, camino[1:]):
            self.assertIn(siguiente, generar_orillas(actual))


if __name__ == "__main__":
    unittest.main()
