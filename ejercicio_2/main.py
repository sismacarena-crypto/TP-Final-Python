"""Ejercicio 2: inventario orientado a objetos y persistencia JSON."""
import json
from pathlib import Path


class StockInvalidoError(Exception):
    """Error de negocio para cantidades de stock negativas."""


class DispositivoEcologico:
    def __init__(self, modelo, precio, stock):
        self.modelo = modelo
        self.precio = float(precio)
        self.set_stock(stock)

    def get_stock(self):
        return self.__stock

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or isinstance(nuevo_stock, bool):
            raise StockInvalidoError("El stock debe ser un número entero")
        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo")
        self.__stock = nuevo_stock

    def obtener_ficha_tecnica(self):
        return f"Modelo: {self.modelo} | Precio: ${self.precio:.2f} | Stock: {self.get_stock()}"

    def a_diccionario(self):
        return {"tipo": "DispositivoEcologico", "modelo": self.modelo, "precio": self.precio, "stock": self.get_stock()}


class PanelSolar(DispositivoEcologico):
    def __init__(self, modelo, precio, stock, eficiencia_watts):
        super().__init__(modelo, precio, stock)
        self.eficiencia_watts = eficiencia_watts

    def obtener_ficha_tecnica(self):
        return f"{super().obtener_ficha_tecnica()} | Potencia: {self.eficiencia_watts} W"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos.update({"tipo": "PanelSolar", "eficiencia_watts": self.eficiencia_watts})
        return datos


class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump([dispositivo.a_diccionario() for dispositivo in lista_dispositivos], archivo, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    catalogo = [DispositivoEcologico("Termostato-Pro", 350, 8), PanelSolar("SolarMax-500", 1500, 10, 500)]
    try:
        catalogo[0].set_stock(-5)
    except StockInvalidoError as error:
        print(f"Error controlado: {error}")
    for dispositivo in catalogo:
        print(dispositivo.obtener_ficha_tecnica())
    ruta = Path(__file__).with_name("catalogo_ecotech.json")
    GestorInventario().guardar_catalogo_json(catalogo, ruta)
    print(f"Catálogo guardado en: {ruta}")
