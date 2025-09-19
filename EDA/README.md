# Proyecto EDA con Python - Bank Marketing

## Estructura
- `data/` - Datos en bruto (incluye `bank-additional.csv`). Añada `customer-details.xlsx` si lo tiene.
- `notebooks/` - Notebook principal `eda_bank_marketing.ipynb` con el análisis paso a paso.
- `scripts/` - Script Python `eda.py` que replica el análisis de forma reproducible.
- `reports/` - Gráficos y el informe en `report.md` generado manualmente.
- `requirements.txt` - Dependencias del proyecto.

## Cómo ejecutar
1. Clonar el repositorio.
2. Crear un entorno virtual e instalar dependencias: `pip install -r requirements.txt`
3. Colocar `customer-details.xlsx` en `data/` si lo tiene.
4. Abrir `notebooks/eda_bank_marketing.ipynb` en JupyterLab/VSCode y ejecutar las celdas, o bien ejecutar el script:
```
python scripts/eda.py --data data/bank-additional.csv
```
## Objetivos cubiertos
- Transformación y limpieza de datos
- Análisis descriptivo
- Visualizaciones
- Informe explicativo (en `reports/report.md`)
