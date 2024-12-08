import streamlit as st
import pandas as pd
from PIL import Image

# Load Images
header_image = Image.open('header.jpg')  # Replace with your actual header image path

# Sample Medical Database (This can be expanded with more data)
medical_data = {
    "Symptom": ["Fever", "Cough", "Headache", "Sore Throat", "Fatigue", "Nausea", "Chills", "Body Aches", "Dizziness", "Rash"],
    "Possible Condition": ["Flu, COVID-19, Malaria", "Common Cold, Bronchitis", "Migraine, Dehydration", "Tonsillitis, Flu", "Anemia, Overwork", "Food Poisoning, Stress", "Cold, Infection", "Flu, Muscle Strain", "Vertigo, Dehydration", "Skin Allergies, Infections"],
    "General Remedy": [
        "Drink plenty of fluids, rest, take paracetamol.",
        "Stay hydrated, use cough drops, consult if severe.",
        "Take pain relievers, rest in a quiet place.",
        "Gargle with warm salt water, avoid cold food.",
        "Get enough sleep, eat balanced meals, stay hydrated.",
        "Take anti-nausea medicine, avoid heavy foods.",
        "Dress warmly, stay indoors, use warm fluids.",
        "Take pain relievers, rest, use warm compress.",
        "Hydrate, lie down, avoid sudden movements.",
        "Use soothing creams, avoid scratching, consult for severe cases."
    ],
    "Doctor Visit": [
        "If fever persists for more than 3 days or is above 103°F.",
        "If cough lasts more than 2 weeks or blood appears.",
        "If headache is severe and sudden or with vision issues.",
        "If throat swelling blocks breathing or severe pain persists.",
        "If extreme fatigue doesn't improve after rest.",
        "If nausea is prolonged or severe, or vomiting persists.",
        "If chills are accompanied by high fever or body ache.",
        "If pain is unbearable or doesn’t subside with rest.",
        "If dizziness is frequent or causes difficulty with balance.",
        "If rash worsens or spreads rapidly or is associated with fever."
    ]
}

# Convert to DataFrame for ease of use
df = pd.DataFrame(medical_data)

# App Configuration
st.set_page_config(page_title="Medical Recommendation System", layout="wide")

# Title Section
st.markdown("<h1 style='text-align: center; color: black;'>🌟 Medical Recommendation System</h1>", unsafe_allow_html=True)

# Header Image (Reduced Size)
st.image(header_image, use_column_width=False, width=700)  # Adjust width as needed

# Main Content
st.write("Enter or select your symptoms to get general guidance and remedies.")

# Dropdown for Selecting Symptoms
st.subheader("Select a Symptom")
selected_symptom = st.selectbox("Choose a symptom:", df["Symptom"].tolist())

# Recommendations Section
if selected_symptom:
    st.subheader("Recommendations for: " + selected_symptom)
    
    # Find the matching data for selected symptom
    symptom_data = df[df["Symptom"] == selected_symptom].iloc[0]

    st.write(f"**Possible Conditions**: {symptom_data['Possible Condition']}")
    st.write(f"**General Remedy**: {symptom_data['General Remedy']}")
    st.write(f"**When to See a Doctor**: {symptom_data['Doctor Visit']}")
    st.markdown("---")

# Footer
st.sidebar.title("Disclaimer")
st.sidebar.write("""
This system provides general information and is not a substitute for professional medical advice, diagnosis, or treatment. 
Always consult your doctor or qualified healthcare provider for specific medical concerns.
""")


