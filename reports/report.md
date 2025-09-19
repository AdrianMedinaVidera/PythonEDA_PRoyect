# Informe del Análisis Exploratorio (EDA) — Bank Marketing

## Introducción
Este informe resume el análisis exploratorio realizado sobre `bank-additional.csv`. El objetivo es limpiar y transformar los datos, realizar análisis descriptivo y presentar visualizaciones que permitan extraer conclusiones relevantes para las campañas de marketing.

## Resumen de pasos realizados
1. Carga de datos y tipado correcto de columnas (fechas, categóricas, numéricas).
2. Limpieza: tratamiento de valores faltantes y codificación de variables binarias.
3. Análisis descriptivo: medidas de tendencia central y dispersión, distribución por edad, por profesión y tasa de conversión (`y`).
4. Visualizaciones: histogramas, boxplots, heatmap de correlaciones y barras por categoría.
5. Recomendaciones iniciales basadas en los hallazgos.

## Hallazgos (resumen)
- Distribución de edad, duración media de la llamada y tasa de éxito por `contact`.
- Variables macroeconómicas (`emp.var.rate`, `euribor3m`) muestran correlaciones con la variable objetivo que merecen análisis adicional.

> Para ver el análisis completo y las figuras, abra el notebook `notebooks/eda_bank_marketing.ipynb` o ejecute `scripts/eda.py`.

