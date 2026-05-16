# Dataset & Column Mapping for Business Problem Statements

Based on the 9 specific datasets located in the `csv_data/` folder, here is the breakdown of exactly which files and columns you need to query or aggregate to solve each of the 10 business problem statements, along with the Python code to load them.

*Note: Temporal columns like `year`, `quarter`, `from_timestamp`, and `to_timestamp` are available across all 9 CSV files and should be used universally to filter timelines.*

---

### 1. Customer Segmentation
**Goal:** Identify distinct user groups based on spending habits.
* **Target Files & Columns:** 
  * `csv_data/aggregated_user_devices.csv`: `brand`, `user_count`, `percentage`
  * `csv_data/aggregated_insurance.csv`: `transaction_type`, `payment_instrument_type`, `transaction_amount`, `transaction_count`

**Python Code:**
```python
import pandas as pd

# Load the data
df_user_devices = pd.read_csv('csv_data/aggregated_user_devices.csv')
df_insurance = pd.read_csv('csv_data/aggregated_insurance.csv')

# Extract necessary columns
segmentation_devices = df_user_devices[['brand', 'user_count', 'percentage']]
segmentation_transactions = df_insurance[['transaction_type', 'payment_instrument_type', 'transaction_amount', 'transaction_count']]
```

### 2. Fraud Detection
**Goal:** Analyze transaction patterns to spot fraudulent activities.
* **Target Files & Columns:** 
  * `csv_data/map_transaction.csv` & `csv_data/map_insurance.csv`: `transaction_count`, `transaction_amount`, `entity_name`
  * *All Files:* `success`, `code`, `response_timestamp`, `from_timestamp`

**Python Code:**
```python
df_map_trans = pd.read_csv('csv_data/map_transaction.csv')
df_map_ins = pd.read_csv('csv_data/map_insurance.csv')

# Filter for potential fraud/anomalies
fraud_trans = df_map_trans[['entity_name', 'transaction_count', 'transaction_amount', 'success', 'code', 'from_timestamp']]
failed_attempts = fraud_trans[fraud_trans['success'] == False]
```

### 3. Geographical Insights
**Goal:** Understand payment trends at state and district levels.
* **Target Files & Columns:** 
  * `csv_data/map_transaction.csv`: `entity_level`, `entity_name`, `transaction_amount`, `transaction_count`
  * `csv_data/map_user.csv`: `entity_level`, `entity_name`, `registered_users`, `app_opens`

**Python Code:**
```python
df_map_trans = pd.read_csv('csv_data/map_transaction.csv')
df_map_user = pd.read_csv('csv_data/map_user.csv')

geo_transactions = df_map_trans[['entity_level', 'entity_name', 'transaction_amount', 'transaction_count']]
geo_users = df_map_user[['entity_level', 'entity_name', 'registered_users', 'app_opens']]
```

### 4. Payment Performance
**Goal:** Evaluate the popularity of different payment categories.
* **Target Files & Columns:** 
  * `csv_data/top_transaction.csv`: `entity_name`, `rank`, `metric_type`, `transaction_amount`, `transaction_count`
  * `csv_data/aggregated_insurance.csv`: `transaction_type`, `payment_instrument_type`

**Python Code:**
```python
df_top_trans = pd.read_csv('csv_data/top_transaction.csv')
df_agg_ins = pd.read_csv('csv_data/aggregated_insurance.csv')

payment_performance = df_top_trans[['entity_name', 'rank', 'metric_type', 'transaction_amount', 'transaction_count']]
payment_instruments = df_agg_ins[['transaction_type', 'payment_instrument_type', 'transaction_amount']]
```

### 5. User Engagement
**Goal:** Monitor user activity to enhance retention and satisfaction.
* **Target Files & Columns:** 
  * `csv_data/aggregated_user_summary.csv`: `app_opens`, `registered_users`
  * `csv_data/aggregated_user_devices.csv`: `brand`, `user_count`

**Python Code:**
```python
df_user_summary = pd.read_csv('csv_data/aggregated_user_summary.csv')
df_user_devices = pd.read_csv('csv_data/aggregated_user_devices.csv')

user_engagement = df_user_summary[['year', 'quarter', 'registered_users', 'app_opens']]
device_engagement = df_user_devices[['year', 'quarter', 'brand', 'user_count']]
```

### 6. Product Development
**Goal:** Use insights to inform new features and services.
* **Target Files & Columns:** 
  * `csv_data/aggregated_user_devices.csv`: `brand`, `percentage`
  * `csv_data/aggregated_user_summary.csv`: `app_opens`

**Python Code:**
```python
df_user_devices = pd.read_csv('csv_data/aggregated_user_devices.csv')
df_user_summary = pd.read_csv('csv_data/aggregated_user_summary.csv')

product_devices = df_user_devices[['brand', 'percentage']]
product_usage = df_user_summary[['app_opens']]
```

### 7. Insurance Insights
**Goal:** Analyze insurance data to improve offerings.
* **Target Files & Columns:** 
  * `csv_data/aggregated_insurance.csv`: `transaction_type`, `payment_instrument_type`, `transaction_count`, `transaction_amount`
  * `csv_data/map_insurance.csv`: `metric_type`, `transaction_count`, `transaction_amount`, `entity_name`

**Python Code:**
```python
df_agg_ins = pd.read_csv('csv_data/aggregated_insurance.csv')
df_map_ins = pd.read_csv('csv_data/map_insurance.csv')

insurance_aggregates = df_agg_ins[['transaction_type', 'payment_instrument_type', 'transaction_count', 'transaction_amount']]
insurance_geo = df_map_ins[['entity_name', 'metric_type', 'transaction_count', 'transaction_amount']]
```

### 8. Marketing Optimization
**Goal:** Tailor campaigns based on user behavior and patterns.
* **Target Files & Columns:** 
  * `csv_data/map_user.csv`: `entity_name`, `registered_users`
  * `csv_data/map_transaction.csv`: `entity_name`, `transaction_amount`
  * `csv_data/aggregated_user_devices.csv`: `brand`

**Python Code:**
```python
df_map_user = pd.read_csv('csv_data/map_user.csv')
df_map_trans = pd.read_csv('csv_data/map_transaction.csv')

marketing_targets = df_map_user[['entity_name', 'registered_users']]
marketing_spend_patterns = df_map_trans[['entity_name', 'transaction_amount']]
```

### 9. Trend Analysis
**Goal:** Examine transaction trends over time to anticipate demand.
* **Target Files & Columns:** 
  * `csv_data/map_transaction.csv`: `year`, `quarter`, `transaction_amount`, `transaction_count`
  * `csv_data/aggregated_user_summary.csv`: `year`, `quarter`, `registered_users`, `app_opens`

**Python Code:**
```python
df_map_trans = pd.read_csv('csv_data/map_transaction.csv')
df_user_summary = pd.read_csv('csv_data/aggregated_user_summary.csv')

trend_transactions = df_map_trans[['year', 'quarter', 'transaction_amount', 'transaction_count']]
trend_users = df_user_summary[['year', 'quarter', 'registered_users', 'app_opens']]
```

### 10. Competitive Benchmarking
**Goal:** Compare performance against competitors (or internal benchmarking).
* **Target Files & Columns:** 
  * `csv_data/top_transaction.csv`: `rank`, `entity_name`, `transaction_amount`
  * `csv_data/top_user.csv`: `rank`, `entity_name`, `registered_users`

**Python Code:**
```python
df_top_trans = pd.read_csv('csv_data/top_transaction.csv')
df_top_user = pd.read_csv('csv_data/top_user.csv')

benchmarking_trans = df_top_trans[['rank', 'entity_name', 'transaction_amount']]
benchmarking_users = df_top_user[['rank', 'entity_name', 'registered_users']]
```
