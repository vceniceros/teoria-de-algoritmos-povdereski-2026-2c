import math
import unittest


def restar_pares_cartesianos(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def calcular_distancia(p1, p2):
    diferencia = restar_pares_cartesianos(p1, p2)
    return math.sqrt(diferencia[0] ** 2 + diferencia[1] ** 2)

def pares_mas_cercanos(puntos):
    pares = []
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            pares.append((puntos[i], puntos[j]))
    pares.sort(key=lambda par: calcular_distancia(par[0], par[1]))
    return pares[:3]

#--------------------#
#complejidad espacial: O(n²) por el almacenamiento de todos los pares posibles
#complejidad temporal: O(n² log n) por la generación de todos los pares y la ordenación de los mismos



def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


class TestParesMasCercanos(unittest.TestCase):

    def test_basico_cinco_puntos_distancias_distintas(self):
        puntos = [(0, 0), (1, 0), (2, 2), (6, 1), (7, 4)]
        resultado = pares_mas_cercanos(puntos)
        esperado = [
            ((0, 0), (1, 0)),
            ((1, 0), (2, 2)),
            ((0, 0), (2, 2)),
        ]
        self.assertEqual(resultado, esperado)

    def test_triangulo_devuelve_los_tres_pares_posibles(self):
        puntos = [(0, 0), (3, 0), (0, 4)]
        resultado = pares_mas_cercanos(puntos)
        self.assertEqual(len(resultado), 3)
        distancias = [dist(a, b) for a, b in resultado]
        self.assertEqual(distancias, sorted(distancias))

    def test_puntos_duplicados_distancia_cero_primero(self):
        puntos = [(1, 1), (1, 1), (4, 5), (10, 10), (0, 0)]
        resultado = pares_mas_cercanos(puntos)
        primer_par = resultado[0]
        self.assertAlmostEqual(dist(*primer_par), 0.0)

    def test_coordenadas_negativas(self):
        puntos = [(-3, -3), (-3, -2), (5, 5), (-10, -10)]
        resultado = pares_mas_cercanos(puntos)
        self.assertEqual(resultado[0], ((-3, -3), (-3, -2)))

    def test_orden_ascendente_por_distancia(self):
        puntos = [(0, 0), (2, 1), (5, 5), (5, 6), (10, 10), (1, 1), (8, 2)]
        resultado = pares_mas_cercanos(puntos)
        self.assertEqual(len(resultado), 3)
        distancias = [dist(a, b) for a, b in resultado]
        self.assertEqual(distancias, sorted(distancias))

    def test_puntos_colineales(self):
        puntos = [(0, 0), (1, 0), (3, 0), (7, 0), (8, 0)]
        resultado = pares_mas_cercanos(puntos)
        esperado = [
            ((0, 0), (1, 0)),
            ((7, 0), (8, 0)),
            ((1, 0), (3, 0)),
        ]
        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()
