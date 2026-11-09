"""Ejercicio 1: sanitización y análisis de sensores."""

def limpiar_registro_sensor(registro_raw):
    sensor_id = str(registro_raw["sensor_id"]).strip()
    temperatura_texto = (
        str(registro_raw["temperatura"]).strip().upper()
        .replace("°", "").replace("C", "").replace(",", ".").strip()
    )
    try:
        temperatura = float(temperatura_texto)
    except ValueError:
        raise ValueError(f"Temperatura inválida para {sensor_id}: {registro_raw['temperatura']!r}") from None
    ubicacion = str(registro_raw.get("ubicacion") or "Desconocida").strip() or "Desconocida"
    return {"sensor_id": sensor_id, "temperatura": temperatura, "ubicacion": ubicacion}


def generar_resumen_sensores(lista_sensores, umbral_temperatura):
    alertas = [sensor["sensor_id"] for sensor in lista_sensores if sensor["temperatura"] > umbral_temperatura]
    promedio = sum(sensor["temperatura"] for sensor in lista_sensores) / len(lista_sensores) if lista_sensores else 0.0
    return alertas, promedio


if __name__ == "__main__":
    registros = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "31.2°C"},
        {"sensor_id": " SENSOR-003 ", "temperatura": " 28.0 C ", "ubicacion": "Planta Sur"},
    ]
    limpios = [limpiar_registro_sensor(registro) for registro in registros]
    alertas, promedio = generar_resumen_sensores(limpios, 25.0)
    print("=== REPORTE DE SENSORES ===")
    for sensor in limpios:
        print(f"{sensor['sensor_id']} | {sensor['temperatura']:.1f} °C | {sensor['ubicacion']}")
    print(f"Sensores en alerta: {', '.join(alertas) if alertas else 'Ninguno'}")
    print(f"Temperatura promedio: {promedio:.2f} °C")
