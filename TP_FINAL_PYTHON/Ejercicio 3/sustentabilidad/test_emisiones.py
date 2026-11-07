def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    total_emisiones = 0.0  # Corregido: float
    consumo_por_planta = {}

    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
        emisiones = calcular_emisiones_carbono(consumo)

        total_emisiones += emisiones

        if planta not in consumo_por_planta:
            consumo_por_planta[planta] = 0
        consumo_por_planta[planta] += consumo

    planta_mayor_consumo = None
    if consumo_por_planta:
        planta_mayor_consumo = max(
            consumo_por_planta,
            key=consumo_por_planta.get
        )

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumo_por_planta": consumo_por_planta
    }