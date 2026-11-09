from django.test import SimpleTestCase
from .calculos import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(SimpleTestCase):
    def test_calculo_nominal(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100, 0.5), 50.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)

    def test_metricas(self):
        datos = [{"planta": "Norte", "consumo_kwh": 1200}, {"planta": "Sur", "consumo_kwh": 850}, {"planta": "Norte", "consumo_kwh": 1400}]
        resultado = obtener_metricas_consumo(datos)
        self.assertAlmostEqual(resultado["total_emisiones"], 1380)
        self.assertEqual(resultado["planta_top"], "Norte")

    def test_vista_web(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Norte")
