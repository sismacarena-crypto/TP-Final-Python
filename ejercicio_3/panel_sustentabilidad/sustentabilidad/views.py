from django.shortcuts import render
from .calculos import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    registros = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Norte", "consumo_kwh": 1400},
    ]
    contexto = obtener_metricas_consumo(registros)
    return render(request, "sustentabilidad/panel.html", contexto)
