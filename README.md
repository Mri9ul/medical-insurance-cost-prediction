# 🏥 Medical Insurance Cost Prediction

This project uses machine learning to predict **medical insurance charges** based on personal and health-related features such as age, BMI, smoking status, and region.

---

## 📌 Objective

The objective of this project is to:

* Analyze a real-world insurance dataset
* Perform data preprocessing and exploratory data analysis (EDA)
* Train regression models to predict insurance costs
* Compare model performance
* Build an interactive **Streamlit web app** for real-time predictions

---

## 📊 Dataset

The dataset contains **1338 records** with the following features:

* **age** – Age of the individual
* **sex** – Gender (male/female)
* **bmi** – Body Mass Index
* **children** – Number of dependents
* **smoker** – Smoking status (yes/no)
* **region** – Residential region
* **charges** – Medical insurance cost (target variable)

---

## ⚙️ Project Workflow

1. Data loading
2. Data inspection and cleaning
3. Exploratory Data Analysis (EDA)
4. Encoding categorical variables
5. Train-test split
6. Model training:

   * Linear Regression
   * Random Forest Regressor
7. Model evaluation
8. Model comparison
9. Final model selection
10. Model saving
11. Streamlit app development

---

## 🧠 Models Used

* **Linear Regression**
* **Random Forest Regressor (Final Model)**

---

## 📈 Evaluation Metrics

Models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🏆 Results

* Linear Regression achieved moderate performance
* **Random Forest Regressor performed better** with higher accuracy
* Final model achieved approximately:

```text
R² Score ≈ 0.84
```

👉 Random Forest was selected as the final model.

---

## 💡 Key Insights

* Smoking has a **major impact** on insurance charges
* Higher BMI generally leads to higher insurance costs
* Age also plays a significant role in determining charges

---

## 🖥️ Streamlit App

An interactive web app was built using Streamlit.

### Features:

* User enters personal details
* Model predicts insurance cost instantly
* Simple and user-friendly interface

### Run the app:

```bash
streamlit run app.py
```

---



