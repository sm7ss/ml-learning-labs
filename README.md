# 🧪 ML Learning Labs [WIP]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Polars](https://img.shields.io/badge/Polars-1.41%2B-orange?style=for-the-badge&logo=polars&logoColor=white)](https://pola.rs)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Hydra](https://img.shields.io/badge/Hydra-1.3%2B-89CFF0?style=for-the-badge&logo=hydra&logoColor=white)](https://hydra.cc)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13%2B-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)
[![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

> ⚠️ **PROJECT IN ACTIVE DEVELOPMENT**  
> Hands-on Machine Learning with a **production** focus: pipelines, reproducibility, robust validation, and monitoring.

**ML Learning Labs** is my personal laboratory for learning ML from scratch with a production mindset. Here we build **reproducible, configurable, and deployable** code.

---

## 📍 Learning Roadmap (11 Modules)

| Module | Topic                                                                 | Status         |
|--------|-----------------------------------------------------------------------|----------------|
| 0      | **Setup, Structure & Reproducibility** (Poetry, Hydra, linting)       | 🚧 In progress |
| 1      | Understand the Business + **Robust EDA with Polars**                  | 📝 Planned     |
| 2      | Robust Preprocessing (nulls, outliers, contextual scaling)            | 📝 Planned     |
| 3      | Feature Engineering (when original features aren't enough)            | 📝 Planned     |
| 4      | Baseline + Metrics with Business Context                              | 📝 Planned     |
| 5      | Validation That Doesn't Lie (stratified CV, leakage detection)        | 📝 Planned     |
| 6      | Deep Imbalance Handling                                               | 📝 Planned     |
| 7      | Advanced Models (trees, boosting, ensembles)                          | 📝 Planned     |
| 8      | Model Optimization & Selection                                        | 📝 Planned     |
| 9      | Pipelines with Prefect / Metaflow                                     | 📝 Planned     |
| 10     | Interpretability & Explainability                                     | 📝 Planned     |
| 11     | Production, Monitoring & Drift                                        | 📝 Planned     |

> 🐥 The order is designed to build on **solid foundations** before touching complex models.

---

## 🧱 Module 0 – Setup & Reproducibility

| Feature                        | What it does                                                            |
|--------------------------------|-------------------------------------------------------------------------|
| **Poetry**                     | Dependency management with pinned versions                              |
| **Hydra + OmegaConf**          | Nested and modular configuration (YAML → dict)                          |
| **Pydantic**                   | Configuration validation                                                |
| **GitHub Actions ([lint.yaml](./.github/workflows/lint.yaml))** | Automatic linting on every push                         |
| **Modular structure**          | Clean separation: `config/`, `src/`, `data/`                  |

> 🐥 Everything I learn in [1_hydra_learning/](./1_hydra_learning/) is later applied in [project/](./project/)

### 🔍 Hydra Learning ([1_hydra_learning](./1_hydra_learning/))

Practice folder where I learned to use **Hydra + OmegaConf** before integrating it into the main project.

- Nested configuration ([config.yaml](./1_hydra_learning/config/config.yaml) + overrides)
- Config composition ([data/](./1_hydra_learning/config/data/), [model/](./1_hydra_learning/config/model/))
- Multi-run and hyperparameter sweeps

## 🚧 Coming Soon (Module 1 - EDA with Polars)

- **Fast and efficient** exploratory analysis with Polars
- Null, outlier, and distribution detection
- Automatic report generation (JSON/TXT)
- Hydra integration for configurable parameters

---

## ⚙️ Technologies & Libraries

| Library                | Version      | Purpose                                        |
|------------------------|--------------|------------------------------------------------|
| **Python**             | 3.10+        | Base language                                  |
| **Poetry**             | -            | Dependencies and reproducible environment      |
| **Scikit-learn**       | ≥1.6.0       | Models, metrics, validation                    |
| **Polars**             | ≥1.41.2      | Fast and memory-efficient EDA                  |
| **Hydra-core**         | ≥1.3.2       | Modular configuration (YAML overrides)         |
| **OmegaConf**          | ≥2.3.0       | Nested config management                       |
| **Pydantic**           | ≥2.13.4      | Strong configuration validation                |
| **NumPy**              | 2.2.6        | Base numerical operations                      |
| **PyArrow**            | ≥24.0.0      | Data interchange with Polars                   |
| **Seaborn**            | ≥0.13.2      | Visualization (EDA)                            |
| **Psutil**             | ≥7.2.2       | Resource monitoring (future)                   |

### 🧠 Possible future additions

- `pandas` (only for compatibility with some sklearn utilities)
- `joblib` / `dask` / `Ray` (local parallelization)
- `Metaflow` (pipeline orchestration)
- `Docker` (production containers)

---

## 📁 Project Structure

```text
📂 ml-learning-labs/
├── 📂 .github/
│   ├── 📂 workflows/
│   │   └── lint.yaml                    # Automatic linting
├── 📂 1_hydra_learning/                 # Hydra Learning
│   ├── 📂 config/
│   │   ├── 📂 data/
│   │   │   └── data.yaml                # Data configuration
│   │   ├── 📂 model/
│   │   │   ├── decision_tree.yaml
│   │   │   ├── decision_tree_regressor.yaml
│   │   │   └── random_forest.yaml
│   │   └── config.yaml                  # Main config
│   ├── 📂 src/
│   │   └── main.py
├── 📂 project/                          # Main project (all modules)
│   ├── 📂 config/
│   │   ├── 📂 data/
│   │   │   └── data.yaml                # Data configuration
│   │   ├── 📂 model/
│   │   │   ├── decision_tree_classifier.yaml
│   │   │   ├── decision_tree_regressor.yaml
│   │   │   └── random_forest_classifier.yaml
│   │   └── config.yaml                  # Main config
│   ├── 📂 src/
│   │   ├── 📂 validation/
│   │   │   ├── config_validation.py      # General configuration validation
│   │   │   ├── data_validation.py        # Data configuration validation
│   │   │   └── model_validation.py       # Model configuration validation
├── .gitignore
├── LICENSE
├── main.py                               # Project entry point
├── poetry.lock
├── pyproject.toml
├── README-ESP.md
└── README.md
```

---

## 🖥️ Usage

### Prerequisites

- Python 3.10 or higher
- Poetry installed

### Installation

```bash 
# Clone the repository
git clone https://github.com/sm7ss/ml-learning-labs.git
cd ml-learning-labs

# Install dependencies with Poetry
poetry install

# Activate virtual environment
poetry shell

# Run (depending on the module)
python main.py                           # Main project
python 1_hydra_learning/src/main.py      # Hydra example
```

### Run linting

```bash 
poetry run ruff check .
```

---

## 🎯 Learning Methodology

Each module follows this pattern:

1. Minimal necessary theory (documentation in the README)
2. Hands-on exercise with real or synthetic datasets
3. Robust implementation (configurable, testable, reproducible)

> 🐥 The approach is learning by doing, but without shortcuts. Each concept is deepened with production-grade code.

--- 

## 🧠 AI-Assisted Learning

This roadmap was designed with the support of AI assistants to:

- Define an industry-focused study plan
- Review best practices and design patterns
- Debug and optimize code
- Translate theoretical concepts into concrete implementations

> 🐥 The goal is to learn faster, not to delegate critical thinking.

--- 

## 📈 Current Status

| Area	                    | Status            |
|---------------------------|-------------------|
| Hydra Configuration	    | ✅ Learned        |
| Poetry Structure	        | ✅ Implemented    |
| Linting (GitHub Actions)	| ✅ Active         |
| EDA with Polars	        | 🚧 In progress    |
| Preprocessing	            | 📝 Pending        |
| Modeling	                | 📝 Pending        |
| Production / Monitoring	| 📝 Pending        |

--- 

## 🤝 Contributions

This is a **personal learning repository**, but if you have suggestions, advice, or want to point out a mistake, feel free to open an issue or contact me!
All constructive criticism is welcome 🐥✨

--- 

## 📄 License

MIT License - free to use, modify, and share with attribution.

--- 

## 📬 Contact

🐥 **ML Learning Labs**
Active learning project - questions or suggestions via issues or DM.


