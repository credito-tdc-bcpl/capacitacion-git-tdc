/*
================================================================================
INSTITUCIÓN FINANCIERA - DIRECCIÓN GENERAL DE RIESGO DE CRÉDITO
EQUIPO DE POLÍTICAS Y ESTRATEGIAS DE TARJETA DE CRÉDITO (TDC)
================================================================================
ARCHIVO:        calculo_roll_rate.sql
AUTOR:          Jorge Guzmán (Analista Senior de Políticas TDC)
FECHA CREACIÓN: 2026-10-27
ÚLTIMA MODIF:   2026-10-27
OBJETIVO:       Calcular la matriz de transición mensual (Roll Rates) de la 
                cartera de TDC entre buckets de morosidad (Al Corriente, 
                1-29 días, 30-59 días, 60-89 días, 90+ Castigo).
                Permite estimar provisiones IFRS 9 y alertar sobre deterioro.

TABLAS FUENTE:
  - DWH_RIESGO.CARTERA_MENSUAL_TDC (Cuentas, saldos, días de mora, corte)
  - CATALOGOS.BUCKETS_MOROSIDAD (Definición de rangos de días de atraso)

TABLA DESTINO:
  - BI_RIESGO.MATRIZ_ROLL_RATES_TDC (Vista ejecutiva para comité de crédito)

PERIODICIDAD:   Mensual (Ejecutar tras el cierre contable del último día hábil)
================================================================================
HISTORIAL DE CAMBIOS:
v1.0 (2026-10-27) - Versión base con buckets estándar IFRS 9 / CNBV.
================================================================================
*/

WITH estado_mes_anterior AS (
    SELECT 
        id_cuenta,
        corte_mes AS mes_origen,
        saldo_total AS saldo_origen,
        CASE 
            WHEN dias_mora = 0 THEN 'B0_CORRIENTE'
            WHEN dias_mora BETWEEN 1 AND 29 THEN 'B1_1_A_29_DIAS'
            WHEN dias_mora BETWEEN 30 AND 59 THEN 'B2_30_A_59_DIAS'
            WHEN dias_mora BETWEEN 60 AND 89 THEN 'B3_60_A_89_DIAS'
            WHEN dias_mora >= 90 THEN 'B4_DEFAULT_90MAS'
            ELSE 'NO_IDENTIFICADO'
        END AS bucket_origen
    FROM DWH_RIESGO.CARTERA_MENSUAL_TDC
    WHERE corte_mes = DATEADD(month, -1, CURRENT_DATE())
      AND estatus_cuenta IN ('ACTIVA', 'BLOQUEADA_MORA')
),

estado_mes_actual AS (
    SELECT 
        id_cuenta,
        corte_mes AS mes_destino,
        saldo_total AS saldo_destino,
        CASE 
            WHEN dias_mora = 0 THEN 'B0_CORRIENTE'
            WHEN dias_mora BETWEEN 1 AND 29 THEN 'B1_1_A_29_DIAS'
            WHEN dias_mora BETWEEN 30 AND 59 THEN 'B2_30_A_59_DIAS'
            WHEN dias_mora BETWEEN 60 AND 89 THEN 'B3_60_A_89_DIAS'
            WHEN dias_mora >= 90 THEN 'B4_DEFAULT_90MAS'
            ELSE 'NO_IDENTIFICADO'
        END AS bucket_destino
    FROM DWH_RIESGO.CARTERA_MENSUAL_TDC
    WHERE corte_mes = CURRENT_DATE()
      AND estatus_cuenta IN ('ACTIVA', 'BLOQUEADA_MORA', 'CASTIGADA')
)

SELECT 
    ant.mes_origen,
    act.mes_destino,
    ant.bucket_origen,
    act.bucket_destino,
    COUNT(DISTINCT ant.id_cuenta) AS total_cuentas,
    SUM(ant.saldo_origen) AS saldo_origen_total,
    SUM(act.saldo_destino) AS saldo_destino_total,
    -- Tasa de Transición por Saldo (Roll Rate Monetario)
    ROUND(
        SUM(act.saldo_destino) / NULLIF(SUM(ant.saldo_origen), 0) * 100, 
        2
    ) AS pct_roll_rate_saldo
FROM estado_mes_anterior ant
INNER JOIN estado_mes_actual act 
    ON ant.id_cuenta = act.id_cuenta
GROUP BY 
    ant.mes_origen,
    act.mes_destino,
    ant.bucket_origen,
    act.bucket_destino
ORDER BY 
    ant.bucket_origen ASC,
    act.bucket_destino ASC;
