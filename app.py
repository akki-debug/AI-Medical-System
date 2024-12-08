import streamlit as st
import pandas as pd
from PIL import Image

# Load Images
header_image = Image.open('header.jpg')  # Replace with your actual header image path

# Sample Expanded Medical Database
# You can replace this with a CSV or API-based large dataset for real-time updates
medical_data = {
    "Symptom": [
        "Fever", "Cough", "Headache", "Sore Throat", "Fatigue", "Nausea", "Chills", "Body Aches", "Dizziness", "Rash",
        "Chest Pain", "Shortness of Breath", "Back Pain", "Stomach Pain", "Vomiting", "Diarrhea", "Joint Pain", "Muscle Weakness", "Confusion"
    ],
    "Possible Condition": [
        "Flu, COVID-19, Malaria", "Common Cold, Bronchitis, COVID-19", "Migraine, Dehydration", "Tonsillitis, Flu",
        "Anemia, Overwork", "Food Poisoning, Stress", "Cold, Infection", "Flu, Muscle Strain", "Vertigo, Dehydration",
        "Skin Allergies, Infections", "Heart Attack, Angina", "Asthma, Pneumonia", "Herniated Disc, Kidney Stones",
        "Gastritis, Peptic Ulcers", "Gastroenteritis, Stomach Flu", "IBS, Food Intolerance", "Arthritis, Gout", "Muscular Dystrophy",
        "Alzheimer's Disease, Stroke"
    ],
    "General Remedy": [
        "Drink plenty of fluids, rest, take paracetamol.", "Stay hydrated, use cough drops, consult if severe.",
        "Take pain relievers, rest in a quiet place.", "Gargle with warm salt water, avoid cold food.",
        "Get enough sleep, eat balanced meals, stay hydrated.", "Take anti-nausea medicine, avoid heavy foods.",
        "Dress warmly, stay indoors, use warm fluids.", "Take pain relievers, rest, use warm compress.",
        "Hydrate, lie down, avoid sudden movements.", "Use soothing creams, avoid scratching, consult for severe cases.",
        "Seek immediate medical attention if pain is severe and persistent.", "Use inhalers, stay calm, seek urgent care if necessary.",
        "Rest, apply ice packs, avoid heavy lifting.", "Drink plenty of fluids, take antacids, seek medical care if severe.",
        "Eat small meals, avoid irritants, take antacids.", "Stay hydrated, follow BRAT diet (bananas, rice, applesauce, toast).",
        "Rest, apply hot/cold compress, consider anti-inflammatory medication.", "Consult a neurologist for muscle weakness treatment.",
        "Seek immediate medical attention if experiencing confusion, slurred speech, or other stroke symptoms."
    ],
    "Doctor Visit": [
        "If fever persists for more than 3 days or is above 103°F.", "If cough lasts more than 2 weeks or blood appears.",
        "If headache is severe and sudden or with vision issues.", "If throat swelling blocks breathing or severe pain persists.",
        "If extreme fatigue doesn't improve after rest.", "If nausea is prolonged or severe, or vomiting persists.",
        "If chills are accompanied by high fever or body ache.", "If pain is unbearable or doesn’t subside with rest.",
        "If dizziness is frequent or causes difficulty with balance.", "If rash worsens or spreads rapidly or is associated with fever.",
        "If chest pain is severe or persists for more than 5 minutes.", "If breathing difficulties occur or worsen.",
        "If back pain is severe, radiating to legs, or accompanied by loss of control over bladder/bowels.",
        "If abdominal pain is sudden and severe, or accompanied by vomiting or fever.",
        "If vomiting persists for more than 24 hours or contains blood.",
        "If diarrhea lasts for more than 2 days or is accompanied by high fever or blood.",
        "If joint pain is severe, with swelling or inability to move the joint.",
        "If muscle weakness is persistent, worsening, or associated with fatigue.",
        "If confusion or altered mental state is prolonged, or worsens over time."
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



