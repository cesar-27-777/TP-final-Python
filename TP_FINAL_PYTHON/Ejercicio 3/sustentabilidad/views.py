from django.shortcuts import render
from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1500},
        {"planta": "Planta Sur", "consumo_kwh": 2500},
        {"planta": "Planta Centro", "consumo_kwh": 1800},
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 1000},
        {"planta": "Planta Centro", "consumo_kwh": 900},
    ]

    metricas = obtener_metricas_consumo(registros)

    # Lista para la tabla: planta / consumo / emisión
    lista_plantas = []
    for planta, consumo in metricas["consumo_por_planta"].items():
        emision = consumo * 0.4
        lista_plantas.append({
            "planta": planta,
            "consumo": consumo,
            "emision": emision
        })

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "lista_plantas": lista_plantas
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )