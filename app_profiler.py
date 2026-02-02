import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Pako Moretlwe - Professional Profile")

# Collect basic information
name = "Pako Moretlwe"
role_1 = "Honours Student in Electrical and Information Engineering"
role_2 = "Business Analyst Associate Specialist"
institution_1 = "University of the Witwatersrand, Johannesburg"
institution_2 = "Discovery Limited Pty(Ltd)"

# Display basic profile information
st.header("Overview")
st.write(f"**Name:** {name}")
st.write(f"**Academic Role:** {role_1} at {institution_1}")
st.write(f"**Professional Role:** {role_2} at {institution_2}")

st.write("""
I am a dual-focused professional: an Electrical and Information Engineering student passionate about AI/ML applications in industrial settings, 
and a Business Analyst optimizing Tech infrastructure at a leading financial services organization.
""")

st.image(
    "https://www.wits.ac.za/media/wits-university/news-and-events/images/news/2023-sept-dec/ARM%20Building%20600x300px.jpeg",
    caption="Wits Engineering, ARM building"
)

# --- SKILLS SECTION ---
st.header("Skills Matrix")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical & Engineering")
    tech_skills = pd.DataFrame({
        "Skill": ["Python (Pandas, Streamlit)", "Machine Learning (Scikit-learn, TensorFlow)", "Control Systems", "Data Analysis", "Industrial Automation"],
        "Proficiency": [90, 85, 80, 95, 75]
    })
    st.bar_chart(tech_skills.set_index("Skill"))

with col2:
    st.subheader("Business & Strategy")
    biz_skills = pd.DataFrame({
        "Skill": ["Business Analysis", "Requirements Elicitation", "Stakeholder Management", "Process Optimization", "Tech Infrastructure Strategy"],
        "Proficiency": [85, 90, 85, 80, 75]
    })
    st.bar_chart(biz_skills.set_index("Skill"))


# --- FINAL YEAR RESEARCH PROJECT SECTION ---
st.markdown("---")
st.header("Final Year Research Project")
st.subheader("Comparative Study of AI/ML Models for Predicting Gas Emissions in Cement Kilns")

st.write("""
**Objective:** To predict the concentration of Carbon Monoxide (CO) and Nitrous Oxide (NOx) in cement production kilns using historical sensor data.
Accurate prediction helps in optimizing combustion and drastically reducing harmful emissions.
""")

# Mock Data Generation for the Project
models = ["Linear Regression", "Random Forest", "XGBoost", "LSTM (Deep Learning)", "SVM"]
rmse_scores = [12.5, 4.2, 3.8, 3.5, 8.1]
r2_scores = [0.65, 0.89, 0.92, 0.94, 0.78]

performance_df = pd.DataFrame({
    "Model": models,
    "RMSE (Lower is Better)": rmse_scores,
    "R² Score (Higher is Better)": r2_scores
})

st.write("### Model Performance Comparison")
metric = st.radio("Select Metric to Visualize", ["RMSE (Lower is Better)", "R² Score (Higher is Better)"])

st.bar_chart(performance_df.set_index("Model")[metric])

st.write(f"**Insight:** The deep learning model (LSTM) and ensemble methods (XGBoost) significantly outperformed traditional linear models, capturing the non-linear dynamics of the kiln process.")

# Interactive Prediction Demo 
st.write("### Interactive Prediction Analysis")
st.write("Explore how the best performing model tracks actual emissions data over time.")

# Generate time-series data
dates = pd.date_range(start="2024-06-01", periods=100, freq="h")
np.random.seed(42)
actual_co = np.sin(np.linspace(0, 10, 100)) * 50 + 200 + np.random.normal(0, 5, 100)
predicted_co = actual_co + np.random.normal(0, 8, 100) # Add some error

prediction_df = pd.DataFrame({
    "Time": dates,
    "Actual CO Level (ppm)": actual_co,
    "Predicted CO Level (ppm)": predicted_co
})

st.line_chart(prediction_df.set_index("Time"))


# --- PUBLICATIONS SECTION (Legacy) ---
st.markdown("---")
st.header("Publications & Reports")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)
    
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
else:
    st.info("Upload a CSV file to view publications list.")

# --- CONTACT SECTION ---
st.markdown("---")
st.header("Contact Information")
email = "1036161@students.wits.ac.za" # Placeholder
st.write(f"Interested in discussing AI in Industry or Business Tech? Reach out at {email}.")
st.markdown("[LinkedIn Profile](https://www.linkedin.com/) | [GitHub Profile](https://github.com/)")