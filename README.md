# Proyecto end-to-end de Machine Learning con Flask y AWS

Este repositorio implementa un sistema completo de Machine Learning para predecir la esperanza de vida usando el dataset Life Expectancy (WHO). El flujo cubre carga de datos, limpieza, feature engineering, entrenamiento, evaluación, serialización, API con Flask y una base de CI/CD para AWS.

## 1. Objetivo del proyecto

Construir una solución end-to-end de regresión multivariable que permita:
- procesar un dataset real en CSV
- entrenar un modelo de regresión multilineal
- evaluar su desempeño
- serializar el modelo en `model/model.pkl`
- exponer inferencias con Flask en tiempo real
- preparar el proyecto para CI/CD con GitHub, AWS CodeBuild, AWS CodePipeline y AWS Elastic Beanstalk

## 2. Dataset usado

Archivo: `data/life_expectancy_data.csv`

Fuente original: Kaggle, dataset Life Expectancy (WHO). El conjunto contiene 2938 filas y 22 columnas, con datos de 2000 a 2015 para múltiples países. Se reporta además que el dataset integra factores de mortalidad, inmunización, gasto, economía y escolaridad. citeturn458429search1turn688933search11turn688933search8

## 3. Estructura del repositorio

```text
project/
├── data/
│   └── life_expectancy_data.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   └── predict.py
├── app/
│   └── app.py
├── model/
│   ├── model.pkl
│   ├── metadata.json
│   └── metrics.json
├── tests/
│   ├── test_api.py
│   └── test_training.py
├── docs/
│   ├── aws_setup.md
│   ├── ia_documentation_template.md
│   └── video_guide.md
├── .github/workflows/ci.yml
├── buildspec.yml
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

## 4. Preprocesamiento y feature engineering implementado

### Limpieza de datos
- renombrado de columnas a formato limpio en snake_case
- eliminación de filas sin variable objetivo
- validación de tipos numéricos

### Tratamiento de valores faltantes
- imputación por mediana para variables numéricas
- imputación por moda para la variable categórica `status`

### Tratamiento de outliers
- clipping por IQR en las variables numéricas dentro del pipeline para evitar fuga de datos

### Transformación de variables
- one hot encoding para `status`
- estandarización con `StandardScaler`
- transformaciones logarítmicas para variables muy sesgadas como `gdp`, `population`, `measles`, `percentage_expenditure`, entre otras
- creación de variables derivadas:
  - `immunization_mean`
  - `adult_infant_ratio`
  - `gdp_per_capita_proxy`
  - `thinness_gap`

## 5. Entrenamiento y evaluación

Se ejecutan dos experimentos para cumplir con las dos particiones pedidas:
- modelo 1: `linear_regression_70_30`
- modelo 2: `linear_regression_80_20`

Ambos usan `LinearRegression` de scikit-learn. Se guardan métricas de:
- RMSE
- MAE
- R²

El mejor experimento se serializa como `model/model.pkl`.

### Resultados obtenidos en esta base
- `linear_regression_70_30`: RMSE 3.5817, MAE 2.6913, R² 0.8626
- `linear_regression_80_20`: RMSE 3.4020, MAE 2.5786, R² 0.8662

El mejor modelo en esta versión fue `linear_regression_80_20`.

## 6. Cómo ejecutar el proyecto

### Crear ambiente e instalar dependencias
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Entrenar el modelo
```bash
python -m src.train --data_path data/life_expectancy_data.csv
```

### Probar API Flask en local
```bash
python app/app.py
```

### Ejemplo de petición
Endpoint:
```text
POST /predict
```

JSON de entrada:
```json
{
  "year": 2015,
  "status": "Developing",
  "adult_mortality": 263.0,
  "infant_deaths": 62,
  "alcohol": 0.01,
  "percentage_expenditure": 71.27962362,
  "hepatitis_b": 65.0,
  "measles": 1154,
  "bmi": 19.1,
  "under_five_deaths": 83,
  "polio": 6.0,
  "total_expenditure": 8.16,
  "diphtheria": 65.0,
  "hiv_aids": 0.1,
  "gdp": 584.25921,
  "population": 33736494.0,
  "thinness_1_19_years": 17.2,
  "thinness_5_9_years": 17.3,
  "income_composition_of_resources": 0.479,
  "schooling": 10.1
}
```

Respuesta:
```json
{
  "prediction": 64.24
}
```

## 7. Pruebas

El proyecto incluye pruebas automáticas:
- endpoint `/health`
- endpoint `/predict`
- entrenamiento y generación de artefactos

Ejecutar:
```bash
pytest -q
```

## 8. CI/CD propuesto

### GitHub Actions
Se incluye `.github/workflows/ci.yml` para:
- instalar dependencias
- entrenar el modelo
- correr pruebas

### AWS
Se incluye `buildspec.yml` para CodeBuild y el proyecto es compatible con Elastic Beanstalk usando `Procfile`. AWS documenta que Elastic Beanstalk para Python usa Gunicorn por defecto y que también puede configurarse con `Procfile`. AWS también indica que CodePipeline debe tener como mínimo una etapa de origen y otra de compilación o despliegue, y que CodeBuild toma instrucciones desde `buildspec.yml`. Además, CodePipeline puede desplegar a Elastic Beanstalk y conectarse a GitHub mediante GitHub App. citeturn836773search2turn836773search0turn836773search3turn836773search9turn480934search9turn480934search1

Pipeline recomendado:
1. Source: GitHub
2. Build: AWS CodeBuild
3. Deploy: AWS Elastic Beanstalk

La guía paso a paso está en `docs/aws_setup.md`.

## 9. Documentación de IA

La plantilla para la documentación de IA está en:
- `docs/ia_documentation_template.md`

## 10. Guía para el video

Se incluye una guía para cubrir los puntos de la rúbrica en:
- `docs/video_guide.md`

## 11. Nota importante sobre el uso de IA

Este repositorio te sirve como base funcional y de estudio. Si lo entregas sin cambios, es muy probable que el porcentaje de código asistido por IA supere el límite permitido por tu profesor. Para sí cumplir con la rúbrica, te conviene:
- reescribir manualmente una parte importante del código
- explicar cada archivo con tus propias palabras
- documentar exactamente qué se tomó como apoyo de IA
- probar cada sección y guardar evidencia
