# =====================================================
# EJERCICIO 2: Modelo Productos, Excepciones y Persistencia
# =====================================================
import json

# --------------------------
# Punto A.1: Excepción personalizada
# --------------------------
class StockInvalidoError(Exception):
    """Excepción que se lanza cuando el stock es negativo"""
    pass

# --------------------------
# Punto A.2: Clase Base DispositivoEcologico
# --------------------------
class DispositivoEcologico:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        # Usamos el setter para validar el stock
        self.set_stock(stock)

    # Getters (encapsulamiento)
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Setter con validación obligatoria
    def set_stock(self, valor):
        if valor < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")
        self.__stock = valor

    # Método base para polimorfismo (ficha técnica)
    def ficha_tecnica(self):
        return (f"Nombre: {self.__nombre} | "
                f"Precio: ${self.__precio} | "
                f"Stock: {self.__stock} unidades")

    # Método para convertir objeto a diccionario (para JSON)
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "precio": self.get_precio(),
            "stock": self.get_stock()
        }

# --------------------------
# Punto A.3: Clase Hija PanelSolar (Herencia + Polimorfismo)
# --------------------------
class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre, precio, stock, potencia, eficiencia):
        super().__init__(nombre, precio, stock)
        self.__potencia = potencia
        self.__eficiencia = eficiencia

    # Sobreescribimos ficha_tecnica → POLIMORFISMO
    def ficha_tecnica(self):
        ficha_base = super().ficha_tecnica()
        return (f"{ficha_base} | "
                f"Potencia: {self.__potencia}W | "
                f"Eficiencia: {self.__eficiencia}")

    # Actualizamos to_dict para agregar los atributos propios
    def to_dict(self):
        dic_base = super().to_dict()
        dic_base["potencia"] = self.__potencia
        dic_base["eficiencia"] = self.__eficiencia
        return dic_base

# --------------------------
# Punto B: Clase GestorInventario + Persistencia JSON
# --------------------------
class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        # Convertir todos los objetos a diccionarios
        lista_diccionarios = [disp.to_dict() for disp in lista_dispositivos]

        # Guardar en el archivo JSON
        with open(ruta_archivo, "w", encoding="utf‑8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4)

        print(f"Catalogo guardado correctamente en: {ruta_archivo}")
        return lista_diccionarios

# --------------------------
# Bloque de Prueba (obligatorio para el TP)
# --------------------------
if __name__ == "__main__":
    gestor = GestorInventario()
    paneles_validos = []

    # Prueba 1: Intentamos crear un panel con stock NEGATIVO (debe capturar el error)
    print("=== PRUEBA STOCK INVALIDO ===")
    try:
        panel_erroneo = PanelSolar("Panel Fallido", 100000, -5, 300, "20%")
    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    # Prueba 2: Creamos paneles VÁLIDOS
    print("\n=== CREACIÓN PRODUCTOS VÁLIDOS ===")
    panel1 = PanelSolar("Panel Solar Eco", 150000, 10, 450, "22%")
    panel2 = PanelSolar("Panel Solar Premium", 200000, 5, 550, "24%")

    paneles_validos.append(panel1)
    paneles_validos.append(panel2)

    # Mostramos la ficha técnica (polimorfismo en acción)
    print(panel1.ficha_tecnica())
    print(panel2.ficha_tecnica())

    # Prueba 3: Guardar en JSON
    print("\n=== EXPORTACIÓN JSON ===")
    ruta = "catalogo_ecotech.json"
    lista_guardada = gestor.guardar_catalogo_json(paneles_validos, ruta)

    # Imprimir productos guardados (igual a tu salida de terminal)
    print("\nProductos guardados:")
    for producto in lista_guardada:
        print(producto)