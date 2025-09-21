# GDG_Assessment

## Overview

This repository contains the **World Happiness Report (WHR) analysis and prediction project**. It includes:

- **Data cleaning and preprocessing**  
- **Machine learning model training** to predict happiness scores  
- **Streamlit app** for interactive model deployment  
- Saved model, scaler, and preprocessing objects  

The project leverages Python, Pandas, Scikit-learn, and Streamlit.

---

## Repository Structure

```

GDG\_Assessment/
│
├── GDG\_Assessment.ipynb        # Jupyter Notebook for data analysis and model training
├── app.py                      # Streamlit app for model deployment
├── whr\_cleaned\_data/           # Cleaned dataset used for training
├── whr\_best\_model.pkl          # Trained machine learning model
├── whr\_scaler.pkl              # StandardScaler object for numeric features
└── whr\_model\_columns.pkl       # List of feature columns used in the model

````

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Solo-Ojay/GDG_Assessment.git
cd GDG_Assessment
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the environment:

* Windows:

```powershell
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

> Make sure you have Python 3.8+ installed.

---

## Usage

### 1. Run Jupyter Notebook

Open the notebook for exploratory data analysis, feature engineering, and model training:

```bash
jupyter notebook GDG_Assessment.ipynb
```

---

### 2. Run the Streamlit App

The Streamlit app allows users to **input features and get predicted happiness scores**:

```bash
streamlit run app.py
```

* Input numeric features: GDP per capita, social support, healthy life expectancy, freedom to make life choices, year
* Select country and region from dropdowns
* View the predicted happiness score

---

## Data

The dataset is derived from **World Happiness Reports (2015–2023)** and includes features such as:

* `gdp_per_capita`
* `social_support`
* `healthy_life_expectancy`
* `freedom_to_make_life_choices`
* `country`
* `region`

---

## Model

* **Algorithm:** Gradient Boosting / Random Forest / Linear Regression (trained in notebook)

* **Preprocessing:**

  * One-hot encoding for categorical features (`country`, `region`)
  * Standard scaling for numeric features

* Model, scaler, and column metadata are saved as `.pkl` files for deployment.

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m "Add new feature"`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a pull request

---

## License

This project is **open-source** and available under the [MIT License](LICENSE).

---

## Contact

For questions or suggestions, contact **Solo-Ojay**:

* GitHub: [https://github.com/Solo-Ojay](https://github.com/Solo-Ojay)

