"""Lógica de negocio independiente de Django."""

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo energético no puede ser negativo")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    total_emisiones = sum(calcular_emisiones_carbono(r["consumo_kwh"]) for r in registros)
    consumo_por_planta = {}
    for registro in registros:
        planta = registro["planta"]
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + registro["consumo_kwh"]
    planta_mayor = max(consumo_por_planta, key=consumo_por_planta.get) if consumo_por_planta else "Sin datos"
    return {"total_emisiones": total_emisiones, "planta_top": planta_mayor}
