# Repositorio de Políticas y Estrategias de Crédito TDC 💳

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![SQL ANSI / Snowflake](https://img.shields.io/badge/SQL-Snowflake%20%7C%20Oracle-brightgreen.svg)](https://www.snowflake.com/)
[![Área: Riesgo de Crédito](https://img.shields.io/badge/%C3%81rea-Pol%C3%ADticas%20TDC-orange.svg)]()

Repositorio centralizado del equipo de **Políticas y Estrategia de Crédito para Tarjetas de Crédito (TDC)**. Este espacio sirve como biblioteca oficial de scripts de originación, calibración de líneas de crédito, matrices de decisión, monitoreo de cosechas (vintages) e indicadores de riesgo de la cartera.

---

## 📌 Reglas de Convivencia y Operación del Repositorio

Para mantener el orden, la trazabilidad y la seguridad regulatoria del banco:

1. **Estructura por Proyectos e Indicadores:** Cada analista trabaja dentro de su carpeta temática asignada (`originacion/`, `lineas-credito/`, `indicadores-cosechas/`). No edites scripts de otros compañeros sin previa coordinación.
2. **Prohibido subir Datos de Clientes:** Bajo **ninguna circunstancia** se autoriza subir archivos con información de clientes (`.csv`, `.xlsx`, `.parquet`), RFC, buró de crédito ni credenciales (`.env`). Todo dato debe ser procesado localmente o consultado directamente en el Data Warehouse.
3. **El Hábito Diario (`git pull`):** Todas las mañanas antes de iniciar el trabajo, abre tu terminal en VS Code (`Ctrl + Ñ`) y ejecuta:
   ```powershell
   git pull
   ```
4. **Documentación Obligatoria:** Todo script (`.py` o `.sql`) debe iniciar con la cabecera estándar de documentación (ver plantilla en carpeta `ejemplos/`).

---

## 🗂️ Estructura del Repositorio

```text
politicas-credito-tdc/
│
├── .gitignore                      # Protección contra subida de datos confidenciales (.csv, .xlsx, .env)
├── README.md                       # Catálogo general y reglas del equipo
│
├── originacion/                    # Scripts de otorgamiento, scorecuts y matrices de riesgo
│   ├── reglas_score_buro.py
│   └── matriz_capacidad_pago.sql
│
├── lineas-credito/                 # Estrategias de límites: asignación inicial, incrementos (CLI) y decrementos
│   ├── reglas_incremento_lineas.py
│   └── query_elegibilidad_linea.sql
│
├── indicadores-cosechas/           # Monitoreo de vintage, roll rates, morosidad y provisiones
│   ├── seguimiento_cosechas_tdc.sql
│   └── matriz_transicion_roll_rates.py
│
└── ejemplos/                       # Plantillas base con documentación modelo
    ├── calculo_roll_rate.sql
    └── reglas_originacion_tdc.py
```

---

## 📋 Catálogo de Scripts y Responsables

| Carpeta / Script | Objetivo de Política | Tablas Fuente | Periodicidad | Responsable Principal |
| :--- | :--- | :--- | :--- | :--- |
| `originacion/reglas_score_buro.py` | Filtros duros y asignación de tasa según Score Buró | `DWH_RIESGO.SOLICITUDES_TDC` | Diaria / En línea | Analista de Originación |
| `originacion/matriz_capacidad_pago.sql` | Extracción de Razón Deuda-Ingreso (DTI) para límite máx. | `DWH_RIESGO.INFO_FINANCIERA` | Bajo demanda | Analista de Admisión |
| `lineas-credito/reglas_incremento_lineas.py` | Campaña mensual de aumento de línea (CLI proactivo) | `DWH_CARTERA.FACTURACION_TDC` | Mensual (Día 5) | Estratega de Portafolio |
| `indicadores-cosechas/seguimiento_cosechas_tdc.sql` | ICV a 3, 6 y 12 meses por cohorte de colocación | `DWH_RIESGO.HISTORICO_CARTERA` | Mensual (Cierre) | Analista de Monitoreo |
| `indicadores-cosechas/matriz_transicion_roll_rates.py`| Probabilidad de migración de buckets (B0 a B1, B1 a B2) | `DWH_RIESGO.ESTATUS_CUENTAS` | Mensual | Especialista Cuantitativo |

---

## 🚀 Guía de Arranque Rápido para Analistas (5 Comandos)

Si es tu primer día con este repositorio:

```powershell
# 1. Clona el repositorio a tu máquina (solo la primera vez)
git clone https://github.com/tu-organizacion-bancaria/politicas-credito-tdc.git

# 2. Entra a la carpeta
cd politicas-credito-tdc

# 3. Antes de empezar tu día (SIEMPRE):
git pull

# 4. Cuando hayas creado o modificado tu script:
git status
git add .
git commit -m "feat(lineas): se actualiza regla de incremento para cosecha 2026-Q1"
git push
```

---

## 👥 Contacto y Soporte del Equipo
* **Gerencia de Políticas de Tarjetas de Crédito**: `politicas.tdc@banco.com`
* **Canal Teams**: `#Riesgo-Credito-TDC-Git`
* **Horario de sincronización de cartera**: Cierres mensuales a las 18:00 hrs.
