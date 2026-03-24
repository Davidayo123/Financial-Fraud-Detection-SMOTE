import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Fraud Detection | David", layout="wide", page_icon="💳")

# --- SIDEBAR: MOCK TRANSACTION SIMULATOR ---
st.sidebar.title("Risk Analysis")
st.sidebar.markdown("---")
st.sidebar.header("🔍 Transaction Simulator")
st.sidebar.write("Test the model's logic based on top feature weights:")

# Sliders for the top 2 features your model identified
v10_val = st.sidebar.slider("Feature V10 (Risk Factor)", min_value=-10.0, max_value=10.0, value=0.0)
v14_val = st.sidebar.slider("Feature V14 (Risk Factor)", min_value=-10.0, max_value=10.0, value=0.0)
tx_amount = st.sidebar.number_input("Transaction Amount ($)", min_value=0.0, value=150.0)

# Interactive prediction button
if st.sidebar.button("Analyze Transaction"):
    with st.spinner('Analyzing node pathways...'):
        if v10_val < -3.0 and v14_val < -3.0:
            st.sidebar.error(f"FRAUD DETECTED: Blocked ${tx_amount:,.2f}")
        else:
            st.sidebar.success(f"Transaction Approved: ${tx_amount:,.2f}")

# --- MAIN DASHBOARD AREA ---
st.title("Financial Fraud Detection")
st.markdown("Catching anomalies in highly imbalanced credit card data using **SMOTE** and **Threshold Tuning**.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("The 'Accuracy Paradox'")
    st.info("In a dataset where only 0.2% of transactions are fraudulent, a model guessing 'Normal' every time achieves 99.8% accuracy but fails its business objective. This pipeline optimizes for **Recall** instead.")

with col2:
    st.subheader("Why Threshold Tuning?")
    st.write("By lowering the AI's decision threshold from the default 50% to **15%**, we force the model to flag suspicious transactions earlier. This drastically reduces False Negatives (missed fraud) and saves millions in potential losses.")

st.markdown("---")
st.subheader("Model Artifacts & Business Metrics")

# --- DISPLAY SAVED ARTIFACTS ---
tab1, tab2 = st.tabs(["Tuned Confusion Matrix", "Feature Importance"])

with tab1:
    st.write("Visualizing the impact of the 15% probability threshold on True Positives.")
    try:
        st.image("tuned_confusion_matrix.png", use_container_width=True)
    except FileNotFoundError:
        st.warning("'tuned_confusion_matrix.png' not found. Make sure the image is in the same folder as app.py!")
        
with tab2:
    st.write("Extracting the internal weights of the Random Forest to identify the driving factors of fraud.")
    try:
        st.image("feature_importance_plot.png", use_container_width=True)
    except FileNotFoundError:
        st.warning("'feature_importance_plot.png' not found. Make sure the image is in the same folder as app.py!")
