import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load models
kmeans = pickle.load(open("models/kmeans_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
product_similarity_df = pickle.load(open("models/product_similarity.pkl", "rb"))

cluster_map = {
    2: 'High-Value',
    0: 'Regular',
    3: 'Occasional',
    1: 'At-Risk'
}

st.title("🛒 Shopper Spectrum")

# ================= PRODUCT RECOMMENDATION =================
st.header("📦 Product Recommendation")

product_name = st.text_input("Enter Product Name")

if st.button("Get Recommendations"):
    if product_name in product_similarity_df.index:
        scores = product_similarity_df[product_name].sort_values(ascending=False)
        recommendations = scores[1:6].index.tolist()
        st.success("Recommended Products:")
        for prod in recommendations:
            st.write("•", prod)
    else:
        st.error("Product not found")

# ================= CUSTOMER SEGMENTATION =================
st.header("👤 Customer Segmentation")

recency = st.number_input("Recency (days)", min_value=0)
frequency = st.number_input("Frequency", min_value=0)
monetary = st.number_input("Monetary Value", min_value=0.0)

if st.button("Predict Customer Segment"):
    rfm_input = np.array([[recency, frequency, monetary]])
    rfm_scaled = scaler.transform(rfm_input)
    cluster = kmeans.predict(rfm_scaled)[0]
    segment = cluster_map[cluster]

    st.success(f"Customer Segment: **{segment}**")
