import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import hashlib
from PIL import Image
import time

# User Authentication
def make_hashes(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

# User Database (Mock)
user_data = {
    "username": ["admin", "user1"],
    "password": [make_hashes("admin123"), make_hashes("password")]
}

# App Configuration
st.set_page_config(page_title="AI Treatment Recommendation System", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Menu", ["Home", "Input Details", "Results", "About", "Chatbot"])

# Authentication Logic
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.sidebar.subheader("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in user_data["username"]:
            user_idx = user_data["username"].index(username)
            if check_hashes(password, user_data["password"][user_idx]):
                st.sidebar.success("Login successful!")
                st.session_state["authenticated"] = True
            else:
                st.sidebar.error("Incorrect password.")
        else:
            st.sidebar.error("Username not found.")
else:
    st.sidebar.success("Logged in!")

    # Home Page
    if menu == "Home":
        st.title("🌟 Welcome to the AI Treatment Recommendation System")
        st.image("header.jpg", use_column_width=True, caption="Personalized Healthcare Powered by AI")
        st.write("""
        This app provides AI-based treatment recommendations tailored to your needs.
        **Features:**
        - Easy-to-use interface.
        - AI-driven analysis.
        - Personalized insights.
        - Downloadable recommendations.
        """)
        st.balloons()

    # Input Details Page
    elif menu == "Input Details":
        st.title("Enter Your Medical Details")
        st.write("Fill in the details below:")
        with st.form("Input Form"):
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            symptoms = st.text_area("Symptoms")
            medical_history = st.text_area("Medical History")
            report_file = st.file_uploader("Upload Medical Reports (PDFs or Images)", type=["pdf", "jpg", "png"])
            submit = st.form_submit_button("Submit")

        if submit:
            st.success("Details submitted successfully! Navigate to the 'Results' section.")

    # Results Page
    elif menu == "Results":
        st.title("AI Recommendations")
        st.write("Here are the recommendations based on your data:")
        
        # Simulated Recommendations
        recommendations = {
            "Treatment": ["Therapy A", "Therapy B", "Lifestyle Changes"],
            "Effectiveness (%)": [85, 75, 90]
        }
        df = pd.DataFrame(recommendations)

        # Display Table
        st.table(df)

        # Bar Chart
        fig, ax = plt.subplots()
        ax.bar(df["Treatment"], df["Effectiveness (%)"], color=['blue', 'green', 'orange'])
        ax.set_title("Effectiveness of Recommended Treatments")
        ax.set_xlabel("Treatment")
        ax.set_ylabel("Effectiveness (%)")
        st.pyplot(fig)

        # Downloadable Report
        st.download_button(
            label="Download Recommendations",
            data="Your personalized recommendations: " + df.to_csv(index=False),
            file_name="recommendations.csv",
            mime="text/csv"
        )

    # About Page
    elif menu == "About":
        st.title("About the App")
        st.write("""
        This AI-powered system leverages advanced machine learning models to analyze patient data and suggest personalized treatment plans. Our goal is to assist healthcare providers and patients in making informed decisions.
        """)
        st.image("team.jpg", caption="Our Development Team", use_column_width=True)

    # Chatbot Page
    elif menu == "Chatbot":
        st.title("AI Chatbot Assistant")
        st.write("Ask your health-related questions:")
        with st.form("Chatbot Form"):
            query = st.text_input("Type your query here:")
            submit_query = st.form_submit_button("Ask")

        if submit_query:
            # Simulated chatbot response
            st.write("AI Response: Thank you for your question. We're here to help!")
