import unittest
import sys
import os

# --- ARREGLO DE RUTAS ---
current_dir = os.path.dirname(os.path.abspath(__file__))
# Subimos un nivel y forzamos la entrada a la carpeta 'src'
target_folder = os.path.join(os.path.dirname(current_dir), 'src')
sys.path.insert(0, target_folder)
# ------------------------

from lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test: Reinicia el lavadero."""
        self.lavadero = Lavadero()

    # --- TESTS DE ESTADO INICIAL Y EXCEPCIONES ---

    def test1_estado_inicial_inactivo(self):
        """Test 1: Verifica el estado inicial del lavadero."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)

    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Encerar sin secado a mano debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            self.lavadero._hacer_lavado(prelavado_a_mano=False, secado_a_mano=False, encerado=True)

    def test3_excepcion_lavado_en_marcha(self):
        """Test 3: Iniciar lavado si ya está ocupado lanza RuntimeError."""
        self.lavadero._hacer_lavado(False, False, False) # Ocupamos el lavadero
        with self.assertRaises(RuntimeError):
            self.lavadero._hacer_lavado(True, True, True) # Intentamos entrar con otro

    # --- TESTS DE PRECIOS (INGRESOS) ---

    def test4_precio_con_prelavado(self):
        """Test 4: Prelavado (S), Secado(N), Cera(N) -> 6.50€"""
        self.lavadero._hacer_lavado(True, False, False)
        self.lavadero.avanzarFase() # Al avanzar cobra
        self.assertAlmostEqual(self.lavadero.ingresos, 6.50, places=2)

    def test5_precio_con_secado(self):
        """Test 5: Prelavado (N), Secado(S), Cera(N) -> 6.00€"""
        self.lavadero._hacer_lavado(False, True, False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 6.00, places=2)

    def test6_precio_con_secado_y_encerado(self):
        """Test 6: Prelavado (N), Secado(S), Cera(S) -> 7.20€"""
        self.lavadero._hacer_lavado(False, True, True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 7.20, places=2)

    def test7_precio_con_prelavado_y_secado(self):
        """Test 7: Prelavado (S), Secado(S), Cera(N) -> 7.50€"""
        self.lavadero._hacer_lavado(True, True, False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 7.50, places=2)

    def test8_precio_completo(self):
        """Test 8: Prelavado (S), Secado(S), Cera(S) -> 8.70€"""
        self.lavadero._hacer_lavado(True, True, True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 8.70, places=2)

    # --- TESTS DE FLUJO DE FASES ---

    def test9_flujo_sin_extras(self):
        """Test 9: Sin extras -> 0, 1, 3, 4, 5, 6, 0"""
        esperado = [0, 1, 3, 4, 5, 6, 0]
        obtenido = self.lavadero.ejecutar_y_obtener_fases(False, False, False)
        self.assertEqual(obtenido, esperado, f"Fases erróneas: {obtenido}")

    def test10_flujo_con_prelavado(self):
        """Test 10: Con prelavado -> 0, 1, 2, 3, 4, 5, 6, 0"""
        esperado = [0, 1, 2, 3, 4, 5, 6, 0]
        obtenido = self.lavadero.ejecutar_y_obtener_fases(True, False, False)
        self.assertEqual(obtenido, esperado, f"Fases erróneas: {obtenido}")

    def test11_flujo_con_secado(self):
        """Test 11: Con secado -> 0, 1, 3, 4, 5, 7, 0"""
        esperado = [0, 1, 3, 4, 5, 7, 0]
        obtenido = self.lavadero.ejecutar_y_obtener_fases(False, True, False)
        self.assertEqual(obtenido, esperado, f"Fases erróneas: {obtenido}")

    def test12_flujo_con_secado_y_encerado(self):
        """Test 12: Con secado y cera -> 0, 1, 3, 4, 5, 7, 8, 0"""
        esperado = [0, 1, 3, 4, 5, 7, 8, 0]
        obtenido = self.lavadero.ejecutar_y_obtener_fases(False, True, True)
        self.assertEqual(obtenido, esperado, f"Fases erróneas: {obtenido}")

    def test13_flujo_prelavado_y_secado(self):
        """Test 13: Prelavado y secado -> 0, 1, 2, 3, 4, 5, 7, 0"""
        esperado = [0, 1, 2, 3, 4, 5, 7, 0]
        obtenido = self.lavadero.ejecutar_y_obtener_fases(True, True, False)
        self.assertEqual(obtenido, esperado, f"Fases erróneas: {obtenido}")

    def test14_flujo_completo(self):
        """Test 14: Todo -> 0, 1, 2, 3, 4, 5, 7, 8, 0"""
        esperado = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        obtenido = self.lavadero.ejecutar_y_obtener_fases(True, True, True)
        self.assertEqual(obtenido, esperado, f"Fases erróneas: {obtenido}")

if __name__ == '__main__':
    unittest.main()