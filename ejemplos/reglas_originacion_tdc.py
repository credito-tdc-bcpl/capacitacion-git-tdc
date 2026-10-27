"""
================================================================================
INSTITUCIÓN FINANCIERA - DIRECCIÓN GENERAL DE RIESGO DE CRÉDITO
EQUIPO DE POLÍTICAS Y ESTRATEGIAS DE TARJETA DE CRÉDITO (TDC)
================================================================================
ARCHIVO:        reglas_originacion_tdc.py
AUTOR:          Jorge Guzmán (Analista Senior de Políticas TDC)
FECHA CREACIÓN: 2026-10-27
ÚLTIMA MODIF:   2026-10-27
OBJETIVO:       Motor de reglas de negocio para admisión y originación de 
                Tarjetas de Crédito. Aplica filtros duros de Buró de Crédito,
                capacidad de pago (DTI - Debt to Income) y asignación del límite
                de crédito inicial.

REGLAS DE POLÍTICA (Comité de Riesgos Q4):
  1. Score Buró Mínimo: 650 puntos para producto Clásica, 720 para Oro/Platinum.
  2. DTI Máximo: 40% del ingreso mensual neto comprobable.
  3. Días de mora histórica: 0 cuentas con MOP >= 3 en los últimos 24 meses.
  4. Límite de Crédito: 1.5 a 3.0 veces el ingreso mensual según nivel de riesgo.

ENTRADAS:       Diccionario o DataFrame con variables del solicitante.
SALIDAS:        Diccionario con estatus (APROBADO/RECHAZADO), motivo y límite.
================================================================================
"""

from typing import Dict, Any


def evaluar_solicitud_tdc(solicitud: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evalúa una solicitud de Tarjeta de Crédito contra las reglas de política vigentes.
    
    Parámetros:
        solicitud (dict): Datos del prospecto incluyendo:
            - 'edad' (int): Edad en años
            - 'score_buro' (int): Score crediticio (300 a 850)
            - 'mop_maximo_24m' (int): Peor atraso histórico reportado en Buró
            - 'ingreso_mensual' (float): Ingreso neto comprobado
            - 'deuda_mensual_actual' (float): Compromisos financieros actuales
            - 'producto_deseado' (str): 'CLASICA', 'ORO', 'PLATINUM'
            
    Retorna:
        dict: Dictamen final, motivo de rechazo y límite autorizado sugerido.
    """
    edad = solicitud.get("edad", 0)
    score = solicitud.get("score_buro", 0)
    mop_max = solicitud.get("mop_maximo_24m", 0)
    ingreso = solicitud.get("ingreso_mensual", 0.0)
    deuda = solicitud.get("deuda_mensual_actual", 0.0)
    producto = solicitud.get("producto_deseado", "CLASICA").upper()

    # --- 1. FILTROS DUROS DE POLÍTICA ---
    if edad < 18 or edad > 75:
        return {
            "dictamen": "RECHAZADO",
            "motivo": f"Filtro duro: Edad fuera de rango de política ({edad} años).",
            "limite_autorizado": 0.0
        }

    if mop_max >= 3:
        return {
            "dictamen": "RECHAZADO",
            "motivo": f"Filtro duro: Morosidad grave histórica (MOP {mop_max} >= 3 en 24m).",
            "limite_autorizado": 0.0
        }

    # --- 2. EVALUACIÓN DE SCORE POR PRODUCTO ---
    score_minimo = 720 if producto in ["ORO", "PLATINUM"] else 650
    if score < score_minimo:
        return {
            "dictamen": "RECHAZADO",
            "motivo": f"Score Buró insuficiente para {producto} (Score: {score}, Mínimo: {score_minimo}).",
            "limite_autorizado": 0.0
        }

    # --- 3. REGLA DE CAPACIDAD DE PAGO (DTI - DEBT TO INCOME) ---
    dti_actual = deuda / ingreso if ingreso > 0 else 1.0
    if dti_actual > 0.40:
        return {
            "dictamen": "RECHAZADO",
            "motivo": f"Endeudamiento elevado: DTI actual del {dti_actual*100:.1f}% excede el tope de política (40%).",
            "limite_autorizado": 0.0
        }

    # --- 4. ASIGNACIÓN DE LÍNEA DE CRÉDITO INICIAL ---
    # Multiplicador de ingreso según score
    if score >= 750:
        multiplicador = 2.5
    elif score >= 700:
        multiplicador = 2.0
    else:
        multiplicador = 1.5

    # Límite con tope de prudencia según DTI remanente
    limite_sugerido = round(ingreso * multiplicador, -2) # Redondeado a centenas
    
    # Tope prudencial máximo por producto
    topes = {"CLASICA": 40000.0, "ORO": 80000.0, "PLATINUM": 150000.0}
    limite_final = min(limite_sugerido, topes.get(producto, 40000.0))

    return {
        "dictamen": "APROBADO",
        "motivo": "Cumple filtros duros, score de corte y capacidad de pago.",
        "producto": producto,
        "score_evaluado": score,
        "dti_pre_aprobacion": round(dti_actual, 4),
        "limite_autorizado": limite_final
    }


if __name__ == "__main__":
    # Prueba unitaria de ejemplo con caso de originación
    caso_prueba = {
        "edad": 34,
        "score_buro": 735,
        "mop_maximo_24m": 0,
        "ingreso_mensual": 35000.0,
        "deuda_mensual_actual": 8200.0,
        "producto_deseado": "ORO"
    }
    
    resultado = evaluar_solicitud_tdc(caso_prueba)
    print("=== DICTAMEN DE POLÍTICA DE CRÉDITO TDC ===")
    for k, v in resultado.items():
        print(f"  {k}: {v}")
