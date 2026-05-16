Customer Segmentation using PhonePe Transaction Data 📊
📌 Problem Statement

Customer Segmentation:
Identify distinct user groups based on spending habits to tailor marketing strategies.

📖 Project Overview

This project focuses on analyzing PhonePe insurance transaction data to identify different customer spending behaviors using Exploratory Data Analysis (EDA) and Machine Learning clustering techniques.

The goal is to segment users into meaningful groups based on:

transaction amount
transaction frequency
average transaction value

These insights can help businesses:

personalize marketing campaigns,
improve customer retention,
identify premium users,
and optimize customer engagement strategies.
🛠️ Technologies Used
Python 🐍
Pandas
NumPy
Matplotlib
Scikit-learn
Jupyter Notebook
📂 Dataset Used

Datasets:

aggregated_user_devices.csv
aggregated_insurance.csv

Selected Features:

transaction_amount
transaction_count
brand
user_count
percentage
🔍 Exploratory Data Analysis (EDA)

Performed:

Missing value analysis
Duplicate checking
Statistical summary
Distribution analysis
Brand analysis
Correlation analysis
Feature engineering

Key visualizations:

Transaction amount distribution
Transaction count distribution
Top mobile brands
Cluster visualization
Elbow Method
Silhouette Score analysis
⚙️ Feature Engineering

Created:

avg_transaction_value
log_amount
log_count
log_avg_value

Log transformation was applied to handle:

skewed distributions
large outliers
scale imbalance
🤖 Machine Learning Approach

Algorithm Used:

KMeans Clustering

Preprocessing:

Feature scaling using StandardScaler

Validation Techniques:

Elbow Method
Silhouette Score
📊 Customer Segments Identified

The clustering model identified 4 major customer groups:

Cluster	Customer Type	Characteristics
0	Regular Users	Moderate spending and activity
1	Frequent Small Spenders	High frequency but low transaction value
2	Premium Power Users	Highest spending and transaction activity
3	Low Activity Users	Low engagement and spending
💡 Key Insights
Transaction amount and transaction count showed extremely high correlation (0.989).
Highly engaged users contribute significantly more revenue.
Average transaction value behaves independently from transaction frequency.
Premium users represent the highest-value customer cohort.
Low-activity users may require retention-focused strategies.
