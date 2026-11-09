# Trabajo Práctico Final — Python

Proyecto organizado en tres carpetas, una por ejercicio.

```
TP-Final-Python/
├── ejercicio_1/
│   └── main.py                      # Sanitización de sensores
├── ejercicio_2/
│   ├── main.py                      # Inventario POO + JSON
│   └── catalogo_ecotech.json        # Archivo generado por main.py
└── ejercicio_3/
    └── panel_sustentabilidad/       # Proyecto Django
        ├── manage.py
        ├── requirements.txt
        ├── panel_sustentabilidad/   # Configuración (settings, urls, wsgi, asgi)
        └── sustentabilidad/         # App: calculos.py, views.py, tests.py, templates/
```

## Requisitos

- Python 3.10 o superior
- Django 5.2 (solo para el Ejercicio 3)

Todos los comandos se ejecutan desde la carpeta raíz del repositorio.
En Windows puede usarse `py` en lugar de `python`.

## Ejercicio 1 — Sanitización de sensores (20 puntos)

```bash
python ejercicio_1/main.py
```

- `limpiar_registro_sensor`: quita espacios del identificador, convierte la temperatura
  de texto (`"24.5C"`, `"31.2°C"`, `" 28.0 C "`) a número y asigna `"Desconocida"`
  cuando falta la ubicación.
- `generar_resumen_sensores`: devuelve la lista de sensores que superan el umbral y la
  temperatura promedio.

Salida esperada:

```
=== REPORTE DE SENSORES ===
SENSOR-001 | 24.5 °C | Planta Norte
SENSOR-002 | 31.2 °C | Desconocida
SENSOR-003 | 28.0 °C | Planta Sur
Sensores en alerta: SENSOR-002, SENSOR-003
Temperatura promedio: 27.90 °C
```

## Ejercicio 2 — Inventario y JSON (40 puntos)

```bash
python ejercicio_2/main.py
```

- **Encapsulamiento:** el stock es un atributo privado (`__stock`) con `get_stock` / `set_stock`.
- **Excepción personalizada:** `StockInvalidoError` si el stock es negativo o no es entero.
- **Herencia:** `PanelSolar` hereda de `DispositivoEcologico`.
- **Polimorfismo:** `obtener_ficha_tecnica()` y `a_diccionario()` se redefinen en `PanelSolar`.
- **Persistencia:** `GestorInventario.guardar_catalogo_json()` exporta el catálogo a
  `ejercicio_2/catalogo_ecotech.json`.

## Ejercicio 3 — Pruebas unitarias y Django (40 puntos)

```bash
cd ejercicio_3/panel_sustentabilidad
python -m pip install -r requirements.txt
python manage.py test        # ejecuta las 6 pruebas unitarias
python manage.py migrate     # opcional: crea la base local y evita el aviso de migraciones
python manage.py runserver
```

Luego abrir <http://127.0.0.1:8000/> en el navegador para ver el panel con las emisiones
totales de CO₂ y la planta de mayor consumo.

- `sustentabilidad/calculos.py`: lógica de negocio (`calcular_emisiones_carbono`,
  `obtener_metricas_consumo`), independiente de Django.
- `sustentabilidad/tests.py`: pruebas del cálculo nominal, factor personalizado, consumo
  cero, consumo negativo (`ValueError`), métricas por planta y respuesta de la vista web.
- `sustentabilidad/views.py` y `templates/sustentabilidad/panel.html`: vista y plantilla
  del panel.

Resultado de las pruebas:

```
Ran 6 tests ... OK
```

**Nota:** los registros del panel son datos de ejemplo, no mediciones reales. La clave
secreta y `DEBUG = True` son solo para desarrollo local.
