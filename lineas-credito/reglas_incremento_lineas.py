"""
============================================================
INSTITUCIÓN FINANCIERA - POLÍTICAS DE CRÉDITO TDC
============================================================
ARCHIVO:        reglas_incremento_lineas.py
AUTOR:          Equipo de Estrategias y Límites TDC
FECHA CREACIÓN: 2026-10-27
OBJETIVO:       Reglas de aumento proactivo de línea (CLI)
                para tarjetahabientes al corriente.
============================================================
"""

def es_elegible_incremento(mop_actual: int, antiguedad_meses: int) -> bool:
    """Valida elegibilidad para campaña mensual de aumento de línea."""
    return mop_actual == 0 and antiguedad_meses >= 6
