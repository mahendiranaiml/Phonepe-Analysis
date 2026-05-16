# Customer Segmentation using PhonePe Transaction Data 📊

## 📌 Problem Statement

The objective of this project is to identify distinct customer groups based on transaction behavior using PhonePe transaction data.

Customer segmentation helps businesses:

* Personalize marketing campaigns
* Improve customer retention
* Identify premium customers
* Optimize engagement strategies

---

## 📖 Project Overview

This project analyzes PhonePe insurance transaction data using:

* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Clustering Techniques

The segmentation is based on:

* Transaction Amount
* Transaction Frequency
* Average Transaction Value

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

---

## 📂 Dataset Used

### Datasets

* `aggregated_user_devices.csv`
* `aggregated_insurance.csv`

### Selected Features

* `transaction_amount`
* `transaction_count`
* `brand`
* `user_count`
* `percentage`

---

## 🔍 Exploratory Data Analysis (EDA)

### Analysis Performed

* Missing value analysis
* Duplicate checking
* Statistical summary
* Distribution analysis
* Brand analysis
* Correlation analysis
* Feature engineering

### Key Visualizations

* Transaction amount distribution
* Transaction count distribution
* Top mobile brands
* Cluster visualization
* Elbow Method
* Silhouette Score analysis

---

## ⚙️ Feature Engineering

### Features Created

* `avg_transaction_value`
* `log_amount`
* `log_count`
* `log_avg_value`

### Why Log Transformation?

Log transformation was applied to handle:

* Skewed distributions
* Large outliers
* Scale imbalance

---

## 🤖 Machine Learning Approach

### Algorithm Used

* KMeans Clustering

### Preprocessing

* Feature scaling using `StandardScaler`

### Validation Techniques

* Elbow Method
* Silhouette Score

---

## 📊 Customer Segments Identified

| Cluster | Customer Type           | Characteristics                           |
| ------- | ----------------------- | ----------------------------------------- |
| 0       | Regular Users           | Moderate spending and activity            |
| 1       | Frequent Small Spenders | High frequency but low transaction value  |
| 2       | Premium Power Users     | Highest spending and transaction activity |
| 3       | Low Activity Users      | Low engagement and spending               |

---

## 💡 Key Insights

* Transaction amount and transaction count showed extremely high correlation (`0.989`)
* Highly engaged users contribute significantly more revenue
* Average transaction value behaves independently from transaction frequency
* Premium users represent the highest-value customer cohort
* Low-activity users may require retention-focused strategies

---

## 🚀 Future Improvements

* Apply advanced clustering algorithms like DBSCAN and Hierarchical Clustering
* Build an interactive dashboard
* Perform real-time customer segmentation
* Integrate geographic-level analysis

---

## 📌 Conclusion

This project demonstrates how machine learning can be used to identify meaningful customer groups from transaction data. These insights can support better business decisions, customer targeting, and revenue optimization strategies.

---
