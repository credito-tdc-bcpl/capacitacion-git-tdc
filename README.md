# Portal de Capacitación Git & Monorepos Oficiales TDC 💳

[![GitHub Pages](https://img.shields.io/badge/Portal_Web-GitHub_Pages-blue?style=flat-square&logo=github)](https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/)
[![Organización](https://img.shields.io/badge/Org-credito--tdc--bcpl-2997ff?style=flat-square)](https://github.com/credito-tdc-bcpl)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Polars DataFrames](https://img.shields.io/badge/Polars-0.20%2B-blueviolet?style=flat-square)](https://pola.rs/)
[![DWH Yellowbrick](https://img.shields.io/badge/DWH-Yellowbrick%20SQL-orange?style=flat-square)]()
[![Área: Riesgo de Crédito](https://img.shields.io/badge/%C3%81rea-Pol%C3%ADticas%20TDC-emerald?style=flat-square)]()

Portal interactivo de capacitación técnica y guía de acompañamiento en terminal para el equipo de **Políticas y Estrategias de Tarjetas de Crédito (TDC)** en BanCoppel.

👉 **Accede a la plataforma web interactiva del curso:**  
### 🌐 **[https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/](https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/)**

---

## 🏛️ Ecosistema Oficial de la Organización `credito-tdc-bcpl`

La Dirección de Políticas TDC opera mediante una **arquitectura de 4 repositorios oficiales** por pilar de negocio. Cada científico de datos clona y trabaja en los repositorios donde tiene asignados proyectos:

| Repositorio | Tipo | Stack Principal | Foco Funcional y Alcance |
| :--- | :---: | :--- | :--- |
| [**`originacion-credito`**](https://github.com/credito-tdc-bcpl/originacion-credito) | Privado | Python 3.10+, Polars, Yellowbrick | Modelos probabilísticos, admisión, scoring PD M4, prospección One Click, desentrame SIC (Buró/Círculo) y parametrización de políticas de entrada. *(8 proyectos)* |
| [**`administracion-cartera`**](https://github.com/credito-tdc-bcpl/administracion-cartera) | Privado | Python 3.10+, Polars, Yellowbrick | Mantenimiento de cuentas en vida útil, administración y aumento de líneas (PTCSF-33, incrementos CLI día 11), cancelaciones masivas, reducción de reservas y auditoría de tasas. *(6 proyectos)* |
| [**`indicadores-mensuales-permanentes`**](https://github.com/credito-tdc-bcpl/indicadores-mensuales-permanentes) | Privado | Python 3.10+, Polars, Yellowbrick | Procesos recurrentes de cierre mensual, cosechas (*vintages*), las 5 rutinas mensuales permanentes (BAU), monitoreos normativos y tableros directivos. *(10 procesos)* |
| [**`herramientas-utiles`**](https://github.com/credito-tdc-bcpl/herramientas-utiles) | Privado | Python, Polars, SQL, API Telegram/Trello | Funciones reutilizables de conexión a Yellowbrick (`conexiones-db`), snippets de métricas y fechas (`snippets-python`), queries maestras y automatizaciones internas. |
| [**`capacitacion-git-tdc`**](https://github.com/credito-tdc-bcpl/capacitacion-git-tdc) *(Este repo)* | Público | HTML5, Vanilla CSS / Tailwind, JS Vanilla | Portal educativo de autoservicio para analistas, manual interactivo de comandos, plantillas y generador en vivo. |

---

## 👥 Equipos Oficiales y Matriz de Permisos por Repositorio

Para proteger el código productivo y evitar colisiones entre proyectos, la organización opera con **permisos segregados por equipo**. Cada analista tiene permiso de **Escritura (`Write / Push`)** en el repositorio donde es titular, y de **Lectura (`Read`)** en los demás:

### 🏛️ Los 4 Equipos Oficiales (`credito-tdc-bcpl`)

1. 🎯 **Equipo Originación (`originacion`)**
   * **Integrantes:** Luis Enrique Arriola (`enriquearriola-blip`) y Elizabeth Gómez Soto (`egsoto`).
   * **Permiso de Escritura (`Write`):** [`originacion-credito`](https://github.com/credito-tdc-bcpl/originacion-credito).
   * **Alcance:** Modelos de scoring PD M4, admisión, prospección One Click y reglas de Buró/Círculo.

2. 📊 **Equipo Administración (`administracion`)**
   * **Integrantes:** Armando Morales (`Morales1911`), Laura Anaid Álvarez (`anaidzamudio-tech`) y Andrea Placencia (`aplacencia`).
   * **Permiso de Escritura (`Write`):** [`administracion-cartera`](https://github.com/credito-tdc-bcpl/administracion-cartera).
   * **Alcance:** Mantenimiento de cuentas, PTCSF-33, cortes CLI día 11, cancelaciones y reducción de reservas.

3. 📈 **Equipo Indicadores Recurrentes (`indicadores-recurrentes`)**
   * **Integrantes:** Andrea Placencia (`aplacencia`).
   * **Permiso de Escritura (`Write`):** [`indicadores-mensuales-permanentes`](https://github.com/credito-tdc-bcpl/indicadores-mensuales-permanentes).
   * **Alcance:** Cierres mensuales BAU, cosechas (*vintages*) y tableros directivos.

4. 🔬 **Equipo Certificación (`certificacion`)**
   * **Integrantes:** Naidelin Coronel (`NaiCoronel`), Luis Ernesto Álvarez (`lealvarezfc`) y Juan José López (`jjlopezbc`).
   * **Permiso de Escritura (`Write`):** [`indicadores-mensuales-permanentes`](https://github.com/credito-tdc-bcpl/indicadores-mensuales-permanentes).
   * **Alcance:** Certificación mensual de variables, homologación de tramas SICs en DWH y auditoría cruzada.

---

### 📋 Matriz Oficial de Permisos

| Colaborador | Usuario GitHub | Equipo Oficial | `originacion` | `cartera` | `indicadores` | `herramientas` |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Luis Enrique Arriola** | `@enriquearriola-blip` | Originación | **Write** | Read | Read | Read |
| **Elizabeth Gómez** | `@egsoto` | Originación | **Write** | Read | Read | Read |
| **Armando Morales** | `@Morales1911` | Administración | Read | **Write** | Read | Read |
| **Laura Anaid Álvarez** | `@anaidzamudio-tech` | Administración | Read | **Write** | Read | Read |
| **Andrea Placencia** | `@aplacencia` | Admin & Indicadores | Read | **Write** | **Write** | Read |
| **Naidelin Coronel** | `@NaiCoronel` | Certificación | Read | Read | **Write** | Read |
| **Juan José López** | `@jjlopezbc` | Certificación | Read | Read | **Write** | Read |
| **Luis Ernesto Álvarez** | `@lealvarezfc` | Certificación | Read | Read | **Write** | Read |
| **Jorge Adrián Guzmán** | `@jaguzmanbcpl` | Gerente Políticas TDC | **Admin** | **Admin** | **Admin** | **Admin** |

> **Regla de Colaboración:** Si un analista necesita realizar modificaciones en un repositorio donde tiene acceso de **Lectura**, debe coordinar con los integrantes titulares del repositorio o abrir un **Pull Request** para su revisión y aprobación.

---

## ⚡ Estándar Tecnológico Institucional

Para asegurar la reproducibilidad y el cumplimiento normativo bancario:

1. **Python 3.10+ y Polars:** Todo procesamiento matricial de cartera se realiza con `polars` por su alta velocidad multihilo en millones de cuentas.
2. **Conexión Centralizada a Yellowbrick (`herramientas-utiles`):** Está prohibido incrustar credenciales o cadenas de conexión en tus scripts. Usa siempre el conector oficial:
   ```python
   from conexiones_db.yellowbrick import query_to_polars
   ```
3. **Métricas Homologadas (`snippets-python`):** En los procesos de monitoreo e indicadores, las métricas de morosidad están estandarizadas:
   ```python
   from snippets_python.metricas import calcular_mora_90_plus
   ```
4. **Entornos Virtuales Obligatorios:** Trabaja siempre en tu `.venv` local:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
5. **Blindaje PII (.gitignore):** No se suben extractos `.csv`, `.xlsx`, `.parquet` ni archivos `.env`. Todo dato se consulta directamente a Yellowbrick en tiempo de ejecución.

---

## 💻 Requisito Previo: Instalación de Git en Windows

Si al abrir PowerShell o la consola integrada de VS Code (`Ctrl + Ñ`) y escribir `git --version` aparece el error:
> *"El término 'git' no se reconoce como un nombre de un cmdlet, función, archivo de script o programa ejecutable..."*

Significa que tu equipo aún no tiene Git instalado. Puedes instalarlo directamente en Windows:

### 1. Instalación rápida desde PowerShell (`winget`)
Abre PowerShell y ejecuta:

```powershell
# Instalar el cliente oficial de Git para Windows
winget install --id Git.Git -e --source winget
```

> [!IMPORTANT]
> **REINICIO OBLIGATORIO DE LA TERMINAL:**  
> Tras finalizar la instalación, **debes cerrar PowerShell o reiniciar Visual Studio Code por completo**. Windows necesita recargar las variables de entorno del sistema (`PATH`). Si continúas en la misma ventana abierta, seguirá mostrando el error de que no reconoce el comando.

### 2. Verificar que ya funciona
Abre una terminal limpia y ejecuta:
```powershell
git --version
# Salida esperada: git version 2.4x.x.windows.1
```

*(Alternativa: Si `winget` no estuviera disponible en tu equipo o no tienes permisos, descarga el instalador tradicional de un solo clic desde [git-scm.com/download/win](https://git-scm.com/download/win)).*

---

## 🐣 Flujo Diario de Trabajo en Terminal (PowerShell)

Para actualizar tu código y subir tus avances al repositorio que te corresponde:

```powershell
# 1. Navegar a tu repositorio de trabajo (ejemplo: originacion-credito o administracion-cartera)
cd C:\Users\$env:USERNAME\Documents\GitHub\administracion-cartera

# 2. HÁBITO MATUTINO OBLIGATORIO: Traer los avances del equipo
git pull origin main

# 3. Activar el entorno virtual de Python
.\.venv\Scripts\Activate.ps1

# 4. Verificar el estado de tus archivos modificados
git status

# 5. Agregar tu script modificado dentro de tu submódulo asignado
git add gestion-lineas/incrementos-linea/mi_script.py

# 6. Crear un commit semántico oficial
git commit -m "feat(cartera): actualiza curva de incremento para corte dia 11"

# 7. Publicar tu trabajo de forma segura en GitHub
git push origin main
```

---

## 🔑 Clonación Oficial desde Visual Studio Code (Método sin Administrador)

### ⚠️ ¿Por qué clonar desde la interfaz de VS Code y no por consola?
1. En laptops corporativas, las políticas del banco suelen impedir la instalación de herramientas adicionales en terminal (como `gh`) al requerir permisos de Administrador.
2. Al clonar por terminal, Windows suele utilizar credenciales expiradas o cuentas personales previas, ocasionando el **error 401 Unauthorized** (ante el cual Git elimina la carpeta vacía por seguridad).
3. **Visual Studio Code resuelve todo esto de forma nativa**: gestiona la autenticación con tu cuenta corporativa de GitHub directamente en el navegador web y guarda el acceso seguro en Windows sin necesidad de tokens manuales.

### 🛠️ Paso a paso para clonar cualquier repositorio en VS Code:
1. **Abrir la pantalla de inicio:**
   Abre Visual Studio Code y sitúate en la pestaña **Welcome (Bienvenida / Introducción)**. *(Si no la ves, ve al menú superior: `Ayuda (Help) > Bienvenida (Welcome)`)*.
2. **Iniciar la clonación:**
   En la sección *Comenzar (Start)*, haz clic en **"Clonar repositorio Git..."** (`Clone Git Repository...`).
   *(O presiona el atajo universal: `Ctrl + Shift + P` y escribe `Git: Clonar`).*
3. **Pegar la URL oficial del repositorio:**
   Pega en la barra superior la dirección HTTPS del repositorio en el que trabajarás:
   * **Originación:** `https://github.com/credito-tdc-bcpl/originacion-credito.git`
   * **Administración de Cartera:** `https://github.com/credito-tdc-bcpl/administracion-cartera.git`
   * **Indicadores Permanentes:** `https://github.com/credito-tdc-bcpl/indicadores-mensuales-permanentes.git`
   * **Herramientas Útiles:** `https://github.com/credito-tdc-bcpl/herramientas-utiles.git`
   * **Capacitación:** `https://github.com/credito-tdc-bcpl/capacitacion-git-tdc.git`
4. **Iniciar sesión y autorizar la organización:**
   * VS Code mostrará un aviso: *"¿Permitir que la extensión 'GitHub' inicie sesión mediante GitHub?"*. Haz clic en **Permitir (Allow)**.
   * Se abrirá automáticamente tu navegador web: inicia sesión con tu usuario institucional de BanCoppel (ej. `jaguzmanbcpl`).
   * **Paso crítico de seguridad:** En la pantalla que solicita acceso a la organización `credito-tdc-bcpl`, haz clic en el botón verde **Authorize / Grant**.
5. **Elegir la carpeta destino:**
   Selecciona la carpeta local en tu máquina: `C:\Users\$env:USERNAME\Documents\GitHub` y haz clic en **"Seleccionar como destino del repositorio"**.
6. **Abrir el proyecto:**
   En la notificación emergente inferior derecha de VS Code, haz clic en **Abrir (Open)**.
   *(Al abrirse el proyecto, tu terminal integrada con `Ctrl + Ñ` ya estará lista y sincronizada dentro de la rama `main`).*

---

## 🧭 ¿Cómo usar este Portal de Capacitación?

1. Abre el sitio oficial en tu navegador:  
   👉 **[https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/](https://credito-tdc-bcpl.github.io/capacitacion-git-tdc/)**
2. Consulta la pestaña **"6. Monorepos & Módulos Oficiales"** para:
   - Ver los 4 monorepos y copiar con un clic su URL oficial para clonar en VS Code.
   - Diagnóstico visual y prevención del error 401 Unauthorized sin permisos de administrador.
   - Usar el **Generador Interactivo de Comandos** para obtener la secuencia exacta de terminal para tu módulo y tarea con explicación detallada paso a paso.
   - Acceder a la **Guía de Rescate** ante desincronizaciones (`--rebase`), descartes (`restore`) y auditorías (`diff`, `log`).
3. Avanza por los módulos 1 al 5 para dominar Git desde cero y completar las 9 misiones prácticas en tu consola de Visual Studio Code (`Ctrl + Ñ`).

---

## 👥 Gobernanza y Contacto
* **Gerencia de Políticas de Tarjetas de Crédito**: Jorge Adrián Guzmán Inzunza
* **Organización en GitHub**: [`credito-tdc-bcpl`](https://github.com/credito-tdc-bcpl)
* **Horario de Sincronización BAU**: Cierres mensuales a las 18:00 hrs.
