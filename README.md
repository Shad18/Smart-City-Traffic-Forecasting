🚦 Smart City Traffic Forecasting System
 
Overview

The Smart City Traffic Forecasting System is a Machine Learning project developed to predict vehicle traffic across multiple city junctions using historical traffic data.

The system helps city administrators anticipate traffic peaks, improve traffic management, and support smart city planning initiatives.

---

## Features

✅ Traffic Volume Prediction

✅ Multi-Junction Analysis

✅ Time-Based Traffic Forecasting

✅ Weekend Detection

✅ Holiday Detection

✅ Traffic Risk Classification

✅ Interactive Streamlit Dashboard

✅ Machine Learning Powered Forecasting

---

Dataset

The dataset contains traffic information collected from four city junctions.

Features

* DateTime
* Junction
* Vehicles

Engineered Features

* Hour
* Day
* Month
* DayOfWeek
* Weekend Indicator
* Holiday Indicator
* Rush Hour Indicator

---

Exploratory Data Analysis

The project includes:

* Traffic trend analysis
* Hourly traffic visualization
* Junction-wise traffic comparison
* Weekend vs Weekday analysis

---

Machine Learning Model
Algorithm

Random Forest Regressor

Performance

| Metric   | Score |
| -------- | ----- |
| MAE      | 2.37  |
| R² Score | 0.969 |

The model achieved high prediction accuracy while maintaining good generalization performance.

---

Streamlit Dashboard

The application allows users to:

* Select Junction
* Select Date
* Select Time
* Generate Traffic Predictions

The dashboard also provides:

* Traffic Risk Level
* Traffic Recommendations
* Predicted Vehicle Count

---
Project Structure

SmartCity/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── notebooks/
│   └── traffic_analysis.ipynb
│
├── app.py
├── requirements.txt
└── README.md



Installation

Clone the repository:

git clone https://github.com/Shad18/Smart-City-Traffic-Forecasting.git


Install dependencies:

pip install -r requirements.txt


Run the application:


streamlit run app.py


---

Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Streamlit

---

## Future Improvements

* Weather Integration
* Real-Time Traffic Data
* Deep Learning Models (LSTM)
* Traffic Congestion Heatmaps
* Smart Signal Recommendations

---

## Author

Shadrack Ambrose

Machine Learning & Data Science Internship Project
