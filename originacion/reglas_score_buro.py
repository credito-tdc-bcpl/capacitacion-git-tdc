"""
============================================================
INSTITUCIÓN FINANCIERA - POLÍTICAS DE CRÉDITO TDC
============================================================
ARCHIVO:        reglas_score_buro.py
AUTOR:          Equipo de Políticas de Originación TDC
FECHA CREACIÓN: 2026-10-27
OBJETIVO:       Filtros duros de Score Buró de Crédito
                para admisión de solicitudes TDC.
============================================================
"""

def validar_score_minimo(score: int, producto: str = "CLASICA") -> bool:
    """Verifica si el score cumple con el umbral de política."""
    umbral = 720 if producto in ["ORO", "PLATINUM"] else 650
    return score >= umbral
