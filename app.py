import streamlit as st
import pandas as pd
from PIL import Image

# Load Images
header_image = Image.open('header.jpg')  # Replace with your actual header image path
team_image = Image.open('team.jpg')     # Replace with your actual team image path

# Sample Medical Database (You can replace this with a real API or larger dataset)
medical_data = {
    "Symptom": ["Fever", "Cough", "Headache", "Sore Throat", "Fatigue"],
    "Possible Condition": ["Flu, COVID-19, Malaria", "Common Cold, Bronchitis", "Migraine, Dehydration", "Tonsillitis, Flu", "Anemia, Overwork"],
    "General Remedy": [
        "Drink plenty of fluids, rest, take paracetamol.",
        "Stay hydrated, use cough drops, consult if severe.",
        "Take pain relievers, rest in a quiet place.",
        "Gargle with warm salt water, avoid cold food.",
        "Get enough sleep, eat balanced meals, stay hydrated."
    ],
    "Doctor Visit": [
        "If fever persists for more than 3 days or is above 103°F.",
        "If cough lasts more than 2 weeks or blood appears.",
        "If headache is severe and sudden or with vision issues.",
        "If throat swelling blocks breathing or severe pain persists.",
        "If extreme fatigue doesn't improve after rest."
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
st.write("Enter your symptoms to get general guidance and remedies.")

# Input Section
st.subheader("Input Symptoms")
user_symptoms = st.text_input("Describe your symptoms (e.g., fever, cough):")

if user_symptoms:
    st.subheader("Recommendations")
    # Match symptoms
    matched_data = df[df["Symptom"].str.contains(user_symptoms, case=False)]
    if not matched_data.empty:
        for index, row in matched_data.iterrows():
            st.write(f"**Symptom**: {row['Symptom']}")
            st.write(f"**Possible Conditions**: {row['Possible Condition']}")
            st.write(f"**General Remedy**: {row['General Remedy']}")
            st.write(f"**When to See a Doctor**: {row['Doctor Visit']}")
            st.markdown("---")
    else:
        st.warning("No matches found. Please check your input or consult a doctor for more accurate advice.")

# Team Section
st.subheader("Meet Our Team")
st.image(team_image, use_column_width=True, caption="The team behind this application.")

# Footer
st.sidebar.title("Disclaimer")
st.sidebar.write("""
This system provides general information and is not a substitute for professional medical advice, diagnosis, or treatment. 
Always consult your doctor or qualified healthcare provider for specific medical concerns.
""")

