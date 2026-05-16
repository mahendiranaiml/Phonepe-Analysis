# Customer Segmentation using PhonePe Transaction Data 📊

## 📌 Problem Statement

The objective of this project is to identify distinct customer groups based on transaction behavior using PhonePe transaction data.

Customer segmentation helps businesses:

- Personalize marketing campaigns
- Improve customer retention
- Identify premium customers
- Optimize engagement strategies

---

# 📖 Project Overview

This project analyzes PhonePe insurance transaction data using:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Clustering Techniques

The segmentation is based on:

- Transaction Amount
- Transaction Frequency
- Average Transaction Value

The project successfully identified distinct behavioral customer groups that support data-driven marketing and business decision-making.

---

# 🛠️ Technologies Used

- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

# 📂 Dataset Used

## Datasets

- `aggregated_user_devices.csv`
- `aggregated_insurance.csv`

## Selected Features

- `transaction_amount`
- `transaction_count`
- `brand`
- `user_count`
- `percentage`

---

# 📊 Dataset Statistics

| Metric | Value |
|---|---|
| Total Records | 701 |
| Minimum Transaction Amount | 1,199 |
| Maximum Transaction Amount | 2.29 Billion |
| Average Transaction Amount | 57.1 Million |
| Minimum Transaction Count | 4 |
| Maximum Transaction Count | 1.47 Million |

## 🔍 Key Observation

The dataset showed highly skewed financial distributions with extremely large transaction ranges, making log transformation essential for clustering and analysis.

---

# 🔍 Exploratory Data Analysis (EDA)

## Analysis Performed

- Missing value analysis
- Duplicate checking
- Statistical summary
- Distribution analysis
- Brand analysis
- Correlation analysis
- Feature engineering

## Key Visualizations

- Transaction amount distribution
- Transaction count distribution
- Top mobile brands
- Cluster visualization
- Elbow Method
- Silhouette Score analysis

---

# ⚙️ Feature Engineering

## Features Created

- `avg_transaction_value`
- `log_amount`
- `log_count`
- `log_avg_value`

## Why Log Transformation?

Log transformation was applied to handle:

- Highly skewed distributions
- Large financial outliers
- Scale imbalance
- Better cluster separation

This improved clustering quality by reducing the dominance of extreme transaction values.

---

# 🤖 Machine Learning Approach

## Algorithm Used

- KMeans Clustering

## Preprocessing

- Feature scaling using `StandardScaler`

## Validation Techniques

- Elbow Method
- Silhouette Score

## Clustering Features

The clustering model was trained using:

- Log Transaction Amount
- Log Transaction Count
- Log Average Transaction Value

---

# 📈 Correlation Analysis

| Variables | Correlation |
|---|---|
| Transaction Amount vs Transaction Count | **0.989** |
| Transaction Amount vs Avg Transaction Value | **0.055** |
| Transaction Count vs Avg Transaction Value | **0.018** |

## 💡 Insight

The analysis revealed an extremely strong positive correlation between transaction amount and transaction frequency.

This indicates:

> Highly engaged users contribute significantly more revenue.

Meanwhile, average transaction value showed very weak correlation with transaction frequency, suggesting that repeated engagement matters more than individual high-value transactions.

---

# 📊 Customer Segments Identified

| Cluster | Customer Type | Avg Transaction Amount | Avg Transaction Count | Avg Transaction Value |
|---|---|---|---|---|
| 0 | Regular Users | ~8.0 Million | ~6.9K | ~1314 |
| 1 | Frequent Small Spenders | ~2.0 Million | ~9.3K | ~266 |
| 2 | Premium Power Users | ~149 Million | ~105K | ~1428 |
| 3 | Low Activity Users | ~662K | ~374 | Low |

---

# 💡 Business Insights

## 🔥 Premium Power Users

- Highest revenue-generating customer segment
- Extremely high transaction activity
- Ideal targets for premium insurance plans and loyalty programs

---

## 📈 Frequent Small Spenders

- Highly active but low-value transactions
- Price-sensitive customer group
- Suitable for cashback offers and budget-friendly plans

---

## 🎯 Regular Users

- Stable and consistent transaction behavior
- Strong long-term retention potential
- Good targets for subscription-based offers

---

## ⚠️ Low Activity Users

- Low engagement and low spending
- Potential churn-risk users
- Require re-engagement campaigns and onboarding support

---

# 🚀 Business Impact

The segmentation model can help businesses:

- Personalize marketing campaigns
- Improve customer retention
- Identify high-value customers
- Optimize promotional targeting
- Increase customer engagement
- Design better insurance offerings

---

# ⚠️ Project Limitations

The dataset does not contain:

- Customer IDs
- Individual user history
- Time-based transaction tracking

Therefore, this project performs:

- Behavioral segmentation

instead of:

- Individual customer-level profiling

---

# 📌 Conclusion

This project successfully identified distinct behavioral customer segments using transaction-based features and KMeans clustering.

The analysis demonstrated that:

- Transaction frequency is the strongest driver of revenue generation
- Premium users contribute disproportionately high value
- Customer engagement is more important than individual transaction size

These insights can help businesses make data-driven decisions related to marketing, retention, customer targeting, and revenue optimization.

---
