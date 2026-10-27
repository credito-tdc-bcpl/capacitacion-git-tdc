/*
============================================================
INSTITUCIÓN FINANCIERA - POLÍTICAS DE CRÉDITO TDC
============================================================
ARCHIVO:        seguimiento_cosechas_tdc.sql
AUTOR:          Equipo de Monitoreo de Cartera y Cosechas
FECHA CREACIÓN: 2026-10-27
OBJETIVO:       Cálculo del Índice de Cartera Vencida (ICV)
                a 3, 6 y 12 meses por cohorte de colocación.
============================================================
*/

SELECT 
    DATE_TRUNC('month', fecha_apertura) AS cohorte_colocacion,
    meses_maduracion,
    SUM(saldo_vencido) / NULLIF(SUM(saldo_total), 0) * 100 AS pct_icv
FROM DWH_RIESGO.HISTORICO_CARTERA_TDC
GROUP BY 1, 2
ORDER BY 1 DESC, 2 ASC;
