# --------------------------
# PUNTO A: Función obligatoria
# --------------------------
def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw["sensor_id"].strip()
    temp_texto = registro_raw["temperatura"].replace("°C","").strip()
    temperatura = float(temp_texto)
    ubicacion = registro_raw["ubicacion"].strip()
    if ubicacion == "":
        ubicacion = "Sin ubicación registrada"
    return {"sensor_id": sensor_id, "temperatura": temperatura, "ubicacion": ubicacion}

# --------------------------
# PUNTO B: Función obligatoria (devuelve TUPLA)
# --------------------------
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    alertas = []
    suma = 0
    for s in lista_sensores_limpios:
        suma += s["temperatura"]
        if s["temperatura"] > umbral_temperatura:
            alertas.append(s["sensor_id"])
    promedio = suma / len(lista_sensores_limpios)
    # Devuelve tupla tal cual pide el enunciado
    return (alertas, promedio)

# --------------------------
# Bloque de ejecución
# --------------------------
if __name__ == "__main__":
    datos_crudos = [
        {"sensor_id": " SENSOR‑001 ", "temperatura": "24.5°C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR‑002 ", "temperatura": "35.8°C", "ubicacion": "Planta Sur"},
        {"sensor_id": " SENSOR‑003 ", "temperatura": "42.3°C", "ubicacion": "Planta Central"},
        {"sensor_id": " SENSOR‑004 ", "temperatura": "28.0°C", "ubicacion": ""}
    ]

    # Limpiar cada registro
    sensores_limpios = []
    for reg in datos_crudos:
        sensores_limpios.append(limpiar_registro_sensor(reg))

    umbral = 30.0
    # Llamar a la función B y desempaquetar la tupla
    lista_alertas, promedio_global = generar_resumen_sensores(sensores_limpios, umbral)

    # Imprimir (igual a tu salida de pantalla)
    print("=" * 40)
    print("      INFORME FINAL SENSORES")
    print("=" * 40)
    print("\nSensores procesados:")
    for s in sensores_limpios:
        print(f"{s['sensor_id']} | Temp: {s['temperatura']} °C | Ubicación: {s['ubicacion']}")

    print(f"\nUmbral de alerta establecido: {umbral} °C")
    print(f"Sensores que superan el umbral: {', '.join(lista_alertas)}")
    print(f"Promedio térmico global: {promedio_global:.2f} °C")
    print("\n" + "=" * 40)
    print("          FIN DEL REPORTE")
    print("=" * 40)
