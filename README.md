# Trabajo Práctico Final de Python

Este es mi trabajo práctico final. Está dividido en tres carpetas, una para cada ejercicio.

Para correr los ejercicios hay que tener Python instalado. Todos los comandos se escriben en la terminal, parada en la carpeta principal del proyecto.

## Ejercicio 1: Sensores

En este ejercicio trabajé con datos de sensores de temperatura que venían "sucios", por ejemplo con espacios de más o con la temperatura escrita como texto ("24.5C" o "31.2°C").

Hice dos funciones:

- `limpiar_registro_sensor`: saca los espacios del nombre del sensor, convierte la temperatura a número y, si el sensor no tiene ubicación, le pone "Desconocida".
- `generar_resumen_sensores`: me dice qué sensores pasan la temperatura límite y calcula el promedio.

Para ejecutarlo:

```
python ejercicio_1/main.py
```

## Ejercicio 2: Inventario

Acá hice un pequeño inventario de productos ecológicos usando clases.

- La clase `DispositivoEcologico` guarda el modelo, el precio y el stock. El stock es privado y solo se cambia con `set_stock`, que no deja poner un número negativo.
- Si alguien intenta poner stock negativo, salta un error propio que llamé `StockInvalidoError`.
- La clase `PanelSolar` hereda de `DispositivoEcologico` y le agrega la potencia en watts. También cambia cómo se muestra la ficha técnica.
- `GestorInventario` guarda todos los productos en el archivo `catalogo_ecotech.json`.

Para ejecutarlo:

```
python ejercicio_2/main.py
```

## Ejercicio 3: Pruebas y Django

En este ejercicio hice funciones para calcular las emisiones de carbono a partir del consumo de energía, y les escribí pruebas para ver que funcionen bien (por ejemplo, que den error si el consumo es negativo).

Después armé un proyecto en Django con una página que muestra el total de emisiones y cuál es la planta que más consume. Los datos que usa son de ejemplo, no son mediciones reales.

### Cómo ejecutarlo

1. Entrar a la carpeta del proyecto:

```
cd ejercicio_3/panel_sustentabilidad
```

2. Instalar Django (solo la primera vez):

```
python -m pip install -r requirements.txt
```

3. Correr las pruebas:

```
python manage.py test
```

Si todo está bien, al final aparece `OK`.

4. Prender el servidor:

```
python manage.py runserver
```

5. Abrir en el navegador la dirección `http://127.0.0.1:8000/` para ver la página.

Para apagar el servidor se aprieta `Ctrl + C` en la terminal.

Puede aparecer un aviso de "migraciones sin aplicar". No afecta a la página, pero si se quiere sacar se puede correr `python manage.py migrate`.

## Qué practiqué en este trabajo

- Limpiar datos que vienen escritos de distintas formas y pasarlos a número.
- Usar clases, herencia y atributos privados.
- Crear mi propio tipo de error y atraparlo con `try` / `except`.
- Guardar información en un archivo JSON.
- Escribir pruebas para comprobar que mis funciones den el resultado correcto.
- Armar un proyecto en Django con una vista y una plantilla HTML.
