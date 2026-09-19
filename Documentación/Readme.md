# Lumina Machine Learning Framework

## Objetivo:

El objetivo de este proyecto es tener un framework reutilizable capaz de estandarizar el proceso desde lectura de un archivo de datos, limpieza, análisis exploratorio, modelo y evaluación de modelo.

El Proyecto utiliza un caso de negocio

## Estructura

El Framework tiene la siguiente estructura:

Lumina/
- Documentación/
    - Readme.md
- data/
    - lumina_chocolate_supermercado.csv
-Framework/
    - data_cleaning.py
    - data_loader.py
    - data_validation.py
    - eda.py
    - modelling.py
- Notebooks/
    - Framework_validation.ipynb


Framework/modelling.py contiene las funciones reutilizables de preprocesamiento, división de datos, creación de modelos, validación y selección.

Notebooks/Framework_validation.ipynb utiliza estas funciones para ejecutar y validar el flujo completo.

Flujo de trabajo
Datos
  ↓
Limpieza y exploración
  ↓
División temporal Train/Test
  ↓
Preprocesamiento
  ↓
Entrenamiento
  ↓
Validación cruzada temporal
  ↓
Comparación de modelos
  ↓
Selección del mejor modelo
  ↓
Evaluación final


## Modelos 

Actualmente el framework soporta los siguientes modelos.

- Linear regression
- Lasso regression
- Random Forest
- XGBoost

El framework soporta solamente problemas de regresión.

## Evaluación 

Los modelos son evaluados usando 

- MAE
- RMSE
- MAPE
- R2

El mejor modelo se extrae usando el menor RMSE

