# Repositorio de Políticas y Estrategias de Crédito TDC 💳

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![SQL ANSI / Snowflake](https://img.shields.io/badge/SQL-Snowflake%20%7C%20Oracle-brightgreen.svg)](https://www.snowflake.com/)
[![Área: Riesgo de Crédito](https://img.shields.io/badge/%C3%81rea-Pol%C3%ADticas%20TDC-orange.svg)]()

Repositorio centralizado del equipo de **Políticas y Estrategia de Crédito para Tarjetas de Crédito (TDC)**. Este espacio sirve como biblioteca oficial de scripts de originación, calibración de líneas de crédito, matrices de decisión, monitoreo de cosechas (vintages) e indicadores de riesgo de la cartera.

---

## 🐣 Guía de Instalación y Primer Uso (Para Principiantes Absolutos)

> **¿Es tu primer día usando Git o no sabes si lo tienes instalado?**  
> Sigue estos 5 pasos ordenados para dejar tu entorno listo en menos de 5 minutos y poder abrir el curso interactivo a la par de tu Visual Studio Code.

### Paso 0: Verificar o Instalar Git en Windows

1. Abre la terminal de Windows (**PowerShell**) o abre Visual Studio Code y presiona <kbd>Ctrl</kbd> + <kbd>Ñ</kbd>.
2. Escribe el siguiente comando y presiona <kbd>Enter</kbd>:
   ```powershell
   git --version
   ```
3. **¿Qué resultado obtuviste?**
   - **Caso A (Ya lo tienes):** Aparece algo como `git version 2.4x.x.windows.1`. 👉 Pasa directo al **Paso 1**.
   - **Caso B (No está instalado):** Aparece en rojo *"git no se reconoce como un comando interno o externo..."*.

   **Para instalar Git en Windows (Solo toma 2 minutos):**
   - Opción 1 (Descarga directa): Entra a [https://git-scm.com/download/win](https://git-scm.com/download/win) y descarga el instalador **64-bit Git for Windows Setup**.
   - Opción 2 (Rápida desde PowerShell como Administrador):
     ```powershell
     winget install --id Git.Git -e --source winget
     ```
   - Al instalar, da clic en **"Next"** a todas las opciones por defecto sin cambiar nada.
   - ⚠️ **MUY IMPORTANTE:** Al terminar la instalación, **cierra y vuelve a abrir Visual Studio Code** para que reconozca a Git.

---

### Paso 1: Configurar tu Identidad por Primera Vez (Solo 1 vez en tu máquina)

Para que el banco sepa quién es el autor de cada script o política de crédito, abre la terminal en VS Code (<kbd>Ctrl</kbd> + <kbd>Ñ</kbd>) y ejecuta tus datos:

```powershell
git config --global user.name "Tu Nombre y Apellido"
git config --global user.email "tu.correo@bancoppel.com"
```

---

### Paso 2: Descargar este Repositorio a tu Computadora (`git clone`)

1. En la terminal de Windows o PowerShell, ve a tu carpeta de trabajo preferida (por ejemplo, `Documents`):
   ```powershell
   cd C:\Users\$env:USERNAME\Documents
   ```
2. Descarga la biblioteca completa del equipo con el comando `git clone`:
   ```powershell
   git clone https://github.com/credito-tdc-bcpl/capacitacion-git-tdc.git
   ```
3. Entra a la carpeta recién descargada:
   ```powershell
   cd capacitacion-git-tdc
   ```

---

### Paso 3: Abrir la Carpeta en Visual Studio Code

Desde esa misma terminal, escribe:
```powershell
code .
```
*(O bien abre VS Code, ve al menú superior **Archivo > Abrir Carpeta...** y selecciona la carpeta `capacitacion-git-tdc`).*

Verás todas las carpetas del equipo (`originacion/`, `lineas-credito/`, `indicadores-cosechas/`, `ejemplos/`) en la barra lateral izquierda.

---

### Paso 4: Abrir el Portal de Capacitación Interactivo (`index.html`)

En la raíz de este proyecto tienes el archivo **`index.html`**, que es una plataforma interactiva completa con emuladores de terminal, explicaciones visuales y laboratorios prácticos.

Para abrirlo a la par de tu VS Code:
- **Opción A (Recomendada):** Ábrelo directamente en tu navegador desde GitHub Pages:  
  👉 **[https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/](https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/)**
- **Opción B (Local):** En el explorador lateral de VS Code, dale **clic derecho a `index.html`** ➔ **"Reveal in File Explorer"** y haz doble clic sobre el archivo.

💡 **Tip de trabajo:** Coloca tu navegador en la mitad izquierda de tu pantalla y Visual Studio Code en la mitad derecha. Así podrás leer las lecciones e ir ejecutando los comandos reales en tu terminal.

---

### Paso 5: Tu Primer `git pull` Real en Visual Studio Code

Una vez abierto el proyecto en VS Code:
1. Abre la terminal integrada con el atajo: <kbd>Ctrl</kbd> + <kbd>Ñ</kbd> (o menú **Terminal > New Terminal**).
2. Asegúrate de estar dentro de la carpeta y ejecuta tu primer comando:
   ```powershell
   git pull
   ```
3. Verás la respuesta:
   ```text
   Already up to date.
   ```
¡Felicidades! Tu entorno local está sincronizado con el repositorio central. A partir de este momento, cada mañana antes de comenzar tus análisis, tu primer paso siempre será correr `git pull`.

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
capacitacion-git-tdc/
│
├── index.html                      # Portal web interactivo de capacitación (simulador en navegador)
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

## 🚀 Guía de los 5 Comandos de Supervivencia

Una vez instalado y configurado tu entorno, tu ciclo diario se resume en estos 5 comandos:

```powershell
# 1. Al comenzar el día en tu terminal de VS Code:
git pull

# 2. Cuando hayas terminado de modificar o crear tu script:
git status

# 3. Preparar tus cambios (meter a la caja):
git add .

# 4. Guardar versión con mensaje descriptivo (mínimo 10 caracteres):
git commit -m "feat(lineas): se actualiza regla de incremento para cosecha 2026-Q1"

# 5. Enviar tus cambios a la organización en GitHub:
git push
```

---

## 👥 Contacto y Soporte del Equipo
* **Gerencia de Políticas de Tarjetas de Crédito**: `politicas.tdc@banco.com`
* **Canal Teams**: `#Riesgo-Credito-TDC-Git`
* **Horario de sincronización de cartera**: Cierres mensuales a las 18:00 hrs.
