# Guía sugerida para el video de 12 a 20 minutos

## Meta
Cubrir todos los requerimientos sin errores conceptuales, sin omitir la documentación de IA y mostrando evidencia real.

## Estructura sugerida

### 1. Introducción
Duración sugerida: 1 minuto
- nombre del proyecto
- problema que resuelve
- dataset usado
- por qué se eligió regresión

### 2. Dataset y análisis inicial
Duración sugerida: 2 minutos
- número de filas y columnas
- variable objetivo
- variables numéricas y categóricas
- valores faltantes detectados

### 3. Preprocesamiento y feature engineering
Duración sugerida: 3 minutos
- imputación
- outliers
- encoding
- escalamiento
- transformaciones logarítmicas
- variables derivadas

### 4. Entrenamiento y evaluación
Duración sugerida: 2 minutos
- partición 70/30
- partición 80/20
- comparación de RMSE, MAE y R²
- elección del mejor modelo
- guardado de `model.pkl`

### 5. API con Flask
Duración sugerida: 2 minutos
- enseñar `POST /predict`
- enseñar `GET /health`
- mostrar JSON de entrada
- mostrar respuesta con predicción
- mencionar manejo de errores

### 6. CI/CD y despliegue
Duración sugerida: 2 minutos
- mostrar GitHub
- mostrar GitHub Actions
- mostrar `buildspec.yml`
- mostrar pipeline de AWS
- mostrar Elastic Beanstalk corriendo

### 7. Documentación de IA
Duración sugerida: 2 minutos
- qué partes fueron asistidas
- por qué se usó IA
- qué pruebas se hicieron
- casos límite
- errores corregidos

### 8. Cierre
Duración sugerida: 1 minuto
- conclusión técnica
- aprendizajes del equipo
- posibles mejoras futuras

## Reparto sugerido por integrantes
- persona 1: introducción y dataset
- persona 2: preprocesamiento
- persona 3: entrenamiento y métricas
- persona 4: API y despliegue
- persona 5: documentación de IA y cierre

## Qué no deben olvidar
- hablar con términos correctos
- no leer demasiado
- mostrar evidencia real
- no decir que un modelo es de clasificación si es regresión
- no confundir MAE con RMSE
- no decir que GitHub Actions sustituye a CodePipeline si van a afirmar AWS como CD principal
