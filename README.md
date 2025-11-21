# Seoul Bike Sharing Demand Prediction

## Project Overview

This project implements an end-to-end machine learning solution to predict bike rental demand in Seoul, South Korea. The system analyzes hourly bike rental data along with weather conditions and temporal features to forecast demand patterns.


## Technologies Used

- **Python 3.12+**
- **Data Analysis:** Pandas, NumPy, SciPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Development:** Jupyter Notebook

## Setup Instructions

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/a00017102/MLDA.CW1.17102.git
cd MLDA.CW1.17102
```

2. **Create a virtual environment (recommended):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

3. **Install required packages:**
```bash
pip install -r requirements.txt
```

### Step 1: Train Models (Jupyter Notebook)

Run the Jupyter notebook to perform data analysis and train models:

Execute all cells in order. This will:
- Load and explore the data
- Perform preprocessing and feature engineering
- Train multiple machine learning models
- Evaluate and compare model performance
- Save trained models to the `models/` directory

## Machine Learning Models

Three regression algorithms were implemented and compared:

1. **Random Forest Regressor**
2. **Gradient Boosting Regressor**
3. **Support Vector Regressor (SVR)**

## Model Evaluation Metrics

- **MAE (Mean Absolute Error)** - Average absolute prediction error
- **RMSE (Root Mean Squared Error)** - Penalizes large errors
- **R² Score** - Proportion of variance explained