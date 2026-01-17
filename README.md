# 🛒 Shopper Spectrum  
### Customer Segmentation and Product Recommendation in E-Commerce

**Author:** Kaushik Bora  
**Domain:** E-Commerce Analytics, Machine Learning  
**Tech Stack:** Python, Pandas, NumPy, Scikit-learn, Streamlit  

---

## 📌 Project Overview

The rapid growth of e-commerce platforms has resulted in large volumes of transactional data.  
Analyzing this data effectively can help businesses understand customer behavior, improve retention strategies, and provide personalized product recommendations.

This project focuses on:
- Segmenting customers based on purchasing behavior using **RFM Analysis**
- Identifying meaningful customer groups through **unsupervised learning**
- Building a **product recommendation system** using item-based collaborative filtering
- Deploying the solution through an interactive **Streamlit web application**

---

## 🎯 Objectives

- Perform customer segmentation using Recency, Frequency, and Monetary (RFM) metrics  
- Apply K-Means clustering to identify customer groups  
- Interpret clusters into actionable business segments  
- Recommend similar products based on customer purchase patterns  
- Provide real-time predictions through a web interface  

---

## 📂 Dataset Description

The dataset contains transactional data from an online retail store.

| Column Name   | Description |
|--------------|------------|
| InvoiceNo    | Transaction ID |
| StockCode    | Unique product code |
| Description  | Product name |
| Quantity     | Number of items purchased |
| InvoiceDate  | Date and time of transaction |
| UnitPrice   | Price per unit |
| CustomerID  | Unique customer identifier |
| Country     | Customer’s country |

---

## 🔧 Methodology

### 1️⃣ Data Preprocessing
- Removed missing Customer IDs
- Excluded cancelled transactions
- Filtered invalid quantities and prices
- Created additional features for analysis

### 2️⃣ Exploratory Data Analysis (EDA)
- Country-wise transaction analysis
- Top-selling products identification
- Time-series analysis of transactions
- Distribution analysis of monetary values

### 3️⃣ RFM Analysis
- **Recency:** Days since last purchase  
- **Frequency:** Number of transactions  
- **Monetary:** Total spend per customer  

### 4️⃣ Customer Segmentation
- Standardized RFM features
- Applied **K-Means clustering**
- Used Elbow Method for cluster selection
- Interpreted clusters into business segments:
  - High-Value
  - Regular
  - Occasional
  - At-Risk

### 5️⃣ Product Recommendation System
- Built an item-based collaborative filtering model
- Used cosine similarity on product purchase history
- Recommended top 5 similar products for a given item

---

## 🖥️ Streamlit Web Application

The project includes an interactive Streamlit app with two modules:

### 📦 Product Recommendation
- Input: Product name  
- Output: Top 5 similar products  

### 👤 Customer Segmentation
- Input: Recency, Frequency, Monetary values  
- Output: Predicted customer segment  

---

## 📁 Project Structure

shopper_spectrum/
│── notebooks/
│ └── shopper_spectrum.ipynb
│── models/
│ ├── kmeans_model.pkl
│ ├── scaler.pkl
│ └── product_similarity.pkl
│── app.py
│── requirements.txt
│── README.md


---

## ▶️ How to Run the Project

1. Clone the repository  
2. Create and activate a virtual environment  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

📊 Key Outcomes

Identified meaningful customer segments for targeted marketing

Enabled personalized product recommendations

Built an end-to-end machine learning pipeline

Deployed a real-time interactive application

📌 Conclusion

This project demonstrates the practical application of machine learning techniques in e-commerce analytics.
By combining customer segmentation with recommendation systems, businesses can improve customer engagement, retention, and overall revenue.

👤 Author
Kaushik Bora 