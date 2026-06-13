# 🧪 ML Learning Labs 

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Polars](https://img.shields.io/badge/Polars-1.41%2B-orange?style=for-the-badge&logo=polars&logoColor=white)](https://pola.rs)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Hydra](https://img.shields.io/badge/Hydra-1.3%2B-89CFF0?style=for-the-badge&logo=hydra&logoColor=white)](https://hydra.cc)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13%2B-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)
[![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

> ⚠️ **PROJECT IN ACTIVE DEVELOPMENT**  
> Aprendizaje práctico de Machine Learning con enfoque **producción**: pipelines, reproducibilidad, validación robusta y monitoreo.

**ML Learning Labs** es mi laboratorio personal para aprender ML desde cero pero con mentalidad de producción Aquí se construye **código reproducible, configurable y desplegable**.

--- 

## 📍 Roadmap de Aprendizaje (11 Módulos)

| Módulo | Tema                                                                 | Estado         |
|--------|----------------------------------------------------------------------|----------------|
| 0      | **Setup, Estructura y Reproducibilidad** (Poetry, Hydra, linting)    | 🚧 En curso    |
| 1      | Entender el Negocio + **EDA Robusto con Polars**                     | 📝 Planeado    |
| 2      | Preprocesamiento Robusto (nulos, outliers, escalado contextual)      | 📝 Planeado    |
| 3      | Ingeniería de Features (cuando las features originales no bastan)    | 📝 Planeado    |
| 4      | Baseline + Métricas con Contexto de Negocio                          | 📝 Planeado    |
| 5      | Validación que no miente (CV estratificada, leakage detection)       | 📝 Planeado    |
| 6      | Desbalanceo a fondo                                                  | 📝 Planeado    |
| 7      | Modelos Avanzados (árboles, boosting, ensembles)                     | 📝 Planeado    |
| 8      | Optimización y Selección de Modelos                                  | 📝 Planeado    |
| 9      | Pipelines con Prefect / Metaflow                                     | 📝 Planeado    |
| 10     | Interpretabilidad y Explicabilidad                                   | 📝 Planeado    |
| 11     | Producción, Monitoreo y Drift                                        | 📝 Planeado    |

> 🐥 El orden está pensado para construir **sobre fundamentos sólidos** antes de tocar modelos complejos.

--- 

## 🧱 Módulo 0 – Setup y Reproducibilidad

| Feature                        | Qué hace                                                                 |
|--------------------------------|--------------------------------------------------------------------------|
| **Poetry**                     | Gestión de dependencias con versiones fijas                              |
| **Hydra + OmegaConf**          | Configuración anidada y modular (YAML → dict)                            |
| **Pydantic**                   | Validación de configuraciones                                            |
| **GitHub Actions ([lint.yaml](./.github/workflows/lint.yaml))** | Linting automático en cada push                                          |
| **Estructura modular**         | Separación clara: `config/`, `src/`, `data/`                  |

> 🐥 Todo lo que aprendo en [1_hydra_learning/](./1_hydra_learning/) después se aplica en [project/](./project/)

### 🔍 Hydra Learning ([1_hydra_learning](./1_hydra_learning/))

Carpeta de práctica donde aprendí a usar **Hydra + OmegaConf** antes de integrarlo al proyecto principal.

- Configuración anidada ([config.yaml](./1_hydra_learning/config/config.yaml) + overrides)
- Composición de configs ([data/](./1_hydra_learning/config/data/), [model/](./1_hydra_learning/config/model/))
- Multi-run y barridos de hiperparámetros

## 🚧 Próximamente (Módulo 1 - EDA con Polars)

- Análisis exploratorio **rápido y eficiente** con Polars
- Detección de nulos, outliers, distribuciones
- Generación de reportes automáticos (JSON/TXT)
- Integración con Hydra para parámetros configurables

--- 

## ⚙️ Tecnologías y Librerías

| Librería               | Versión      | Propósito                                      |
|------------------------|--------------|------------------------------------------------|
| **Python**             | 3.10+        | Lenguaje base                                  |
| **Poetry**             | -            | Dependencias y entorno reproducible            |
| **Scikit-learn**       | ≥1.6.0       | Modelos, métricas, validación                  |
| **Polars**             | ≥1.41.2      | EDA rápido y eficiente en memoria              |
| **Hydra-core**         | ≥1.3.2       | Configuración modular (YAML overrides)         |
| **OmegaConf**          | ≥2.3.0       | Gestión de configs anidadas                    |
| **Pydantic**           | ≥2.13.4      | Validación fuerte de configuraciones           |
| **NumPy**              | 2.2.6        | Operaciones numéricas base                     |
| **PyArrow**            | ≥24.0.0      | Intercambio de datos con Polars                |
| **Seaborn**            | ≥0.13.2      | Visualización (EDA)                            |
| **Psutil**             | ≥7.2.2       | Monitoreo de recursos (futuro)                 |

### 🧠 Posibles incorporaciones futuras

- `pandas` (solo para compatibilidad con ciertas utilidades de sklearn)
- `joblib` / `dask` / `Ray` (paralelización local)
- `Metaflow` (orquestación de pipelines)
- `Docker` (contenedores para producción)

--- 

## 📁 Estructura del Proyecto

```text
📂 ml-learning-labs/
├── 📂 .github/
│   └── 📂 workflows/
│       └── lint.yaml                    # Linting automático
├── 📂 1_hydra_learning/                 # Aprendizaje de Hydra
│   ├── 📂 config/
│   │   ├── 📂 data/
│   │   │   └── data.yaml                # Configuración de datos
│   │   ├── 📂 model/
│   │   │   ├── decision_tree.yaml
│   │   │   ├── decision_tree_regressor.yaml
│   │   │   └── random_forest.yaml
│   │   └── config.yaml                  # Config principal
│   ├── 📂 src/
│   │   └── main.py
├── 📂 project/                          # Proyecto principal (todos los módulos)
│   ├── 📂 config//
│   ├── 📂 data/
│   │   ├── train.csv
│   │   └── test.csv
│   ├── 📂 notebooks/                    # Exploración y prototipado
│   └── 📂 src/
├── .gitignore
├── LICENSE
├── main.py     # Entry point del proyecto
├── poetry.lock
├── pyproject.toml
├── README-ESP.md
└── README.md
```

---

## 🖥️ Uso

### Requisitos previos

- Python 3.10 o superior
- Poetry instalado

### Instalación

```bash 

# Clonar el repositorio
git clone https://github.com/sm7ss/ml-learning-labs.git
cd ml-learning-labs

# Instalar dependencias con Poetry
poetry install

# Activar entorno virtual
poetry shell

# Ejecutar (según el módulo)
python main.py                    # Proyecto principal
python 1_hydra_learning/src/main.py  # Ejemplo de Hydra
```

### Ejecutar linting

```bash 
poetry run ruff check .
```

---

## 🎯 Metodología de Aprendizaje

Cada módulo sigue este patrón:

1. Teoría mínima necesaria (documentación en el README)
2. Ejercicio práctico con datasets reales o sintéticos
3. Implementación robusta (configurable, testeable, reproducible)

> 🐥 El enfoque es aprender haciendo, pero sin atajos. Cada concepto se profundiza con código de producción.

--- 

## 🧠 Aprendizaje Asistido por IA

Este roadmap fue diseñado con apoyo de asistentes de IA para:

- Definir un plan de estudios con enfoque industrial
- Revisar buenas prácticas y patrones de diseño
- Depurar y optimizar código
- Traducir conceptos teóricos a implementaciones concretas

> 🐥 El objetivo es aprender más rápido, no delegar el pensamiento crítico.

---

## 📈 Estado Actual

| Área                      | Estado            |
|---------------------------|-------------------|
| Configuración con Hydra	| ✅ Aprendido      |
| Estructura con Poetry	    | ✅ Implementado   |
| Linting (GitHub Actions)	| ✅ Activo         |
| EDA con Polars	        | 🚧 En desarrollo  |
| Preprocesamiento	        | 📝 Pendiente      |
| Modelado	                | 📝 Pendiente      |
| Producción / Monitoreo	| 📝 Pendiente      |

---

## 🤝 Contribuciones

Este es un repositorio **personal de aprendizaje**, pero si tienes sugerencias, consejos o quieres señalar un error, ¡abre un issue o contáctame!
Toda crítica constructiva es bienvenida 🐥✨

---

## 📄 Licencia

MIT License - libre de usar, modificar y compartir con atribución.

--- 

## 📬 Contacto

🐥 **ML Learning Labs**
Proyecto de aprendizaje activo - preguntas o sugerencias por issues o DM.

