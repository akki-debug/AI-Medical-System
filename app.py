import streamlit as st
import pandas as pd

# Example predefined list of drugs with their interactions (simplified for demonstration)
drug_data = {
    "Aspirin": ["Ibuprofen", "Warfarin", "Acetaminophen"],
    "Ibuprofen": ["Aspirin", "Warfarin"],
    "Warfarin": ["Aspirin", "Ibuprofen"],
    "Acetaminophen": ["Aspirin", "Ibuprofen"],
    "Paracetamol": ["Ibuprofen", "Warfarin"],
    "Amoxicillin": ["Penicillin", "Clindamycin"],
    "Clindamycin": ["Amoxicillin", "Penicillin"],
    "Penicillin": ["Amoxicillin", "Clindamycin"]
}

# Expanded symptom-based recommendations with drug suggestions
symptom_recommendations = {
    "Joint Pain": {
        "Possible Conditions": ["Arthritis", "Gout", "Osteoarthritis", "Rheumatoid Arthritis"],
        "General Remedy": "Rest, apply hot/cold compress, consider anti-inflammatory medication.",
        "When to See a Doctor": "If joint pain is severe, with swelling or inability to move the joint.",
        "Drug Recommendations": ["Aspirin", "Ibuprofen", "Diclofenac", "Celecoxib"]
    },
    "Headache": {
        "Possible Conditions": ["Migraine", "Tension headache", "Cluster headache", "Sinusitis"],
        "General Remedy": "Rest, drink plenty of water, avoid bright lights and loud noises.",
        "When to See a Doctor": "If the headache is severe, persistent, or accompanied by vision changes, nausea, or fever.",
        "Drug Recommendations": ["Acetaminophen", "Ibuprofen", "Sumatriptan", "Aspirin"]
    },
    "Stomach Ache": {
        "Possible Conditions": ["Indigestion", "Gastritis", "Gastroenteritis", "Appendicitis", "Irritable Bowel Syndrome"],
        "General Remedy": "Stay hydrated, rest, avoid heavy foods, and consider antacids or mild pain relief.",
        "When to See a Doctor": "If stomach pain is severe, persistent, or associated with vomiting or blood in stool.",
        "Drug Recommendations": ["Omeprazole", "Antacids", "Loperamide", "Diphenoxylate"]
    },
    "Fever": {
        "Possible Conditions": ["Flu", "Cold", "Infection", "COVID-19", "Malaria"],
        "General Remedy": "Stay hydrated, rest, and take fever-reducing medications like paracetamol or ibuprofen.",
        "When to See a Doctor": "If fever exceeds 103°F (39.4°C) or lasts more than 3 days, or is accompanied by severe symptoms.",
        "Drug Recommendations": ["Paracetamol", "Ibuprofen", "Acetaminophen"]
    },
    "Chest Pain": {
        "Possible Conditions": ["Heart Attack", "Angina", "Pneumonia", "Gastroesophageal Reflux Disease (GERD)"],
        "General Remedy": "Rest and avoid physical exertion. Antacids for GERD, and nitroglycerin for angina (if prescribed).",
        "When to See a Doctor": "If chest pain is severe, sudden, and accompanied by shortness of breath, dizziness, or sweating.",
        "Drug Recommendations": ["Aspirin", "Nitroglycerin", "Clopidogrel", "Metoprolol"]
    },
    "Cough": {
        "Possible Conditions": ["Common Cold", "Flu", "Pneumonia", "Chronic Bronchitis"],
        "General Remedy": "Stay hydrated, drink warm liquids, and use cough suppressants or expectorants as needed.",
        "When to See a Doctor": "If the cough persists for more than 3 weeks, is accompanied by blood or mucus, or worsens over time.",
        "Drug Recommendations": ["Dextromethorphan", "Guaifenesin", "Bromhexine", "Codeine"]
    },
    "Shortness of Breath": {
        "Possible Conditions": ["Asthma", "Chronic Obstructive Pulmonary Disease (COPD)", "Heart Failure", "Pulmonary Embolism"],
        "General Remedy": "Use inhalers for asthma or COPD. Avoid exertion and stay calm.",
        "When to See a Doctor": "If shortness of breath occurs suddenly or is associated with chest pain or dizziness.",
        "Drug Recommendations": ["Salbutamol", "Prednisone", "Oxygen therapy", "Ipratropium"]
    },
    "Fatigue": {
        "Possible Conditions": ["Anemia", "Hypothyroidism", "Chronic Fatigue Syndrome", "Depression"],
        "General Remedy": "Ensure adequate rest, balanced diet, and hydration.",
        "When to See a Doctor": "If fatigue is persistent and unexplainable, or accompanied by weakness or unexplained weight loss.",
        "Drug Recommendations": ["Iron supplements", "Thyroxine", "Antidepressants"]
    },
    "Back Pain": {
        "Possible Conditions": ["Muscle Strain", "Herniated Disc", "Sciatica", "Osteoarthritis"],
        "General Remedy": "Rest, hot/cold compress, physical therapy, and over-the-counter pain relievers.",
        "When to See a Doctor": "If the pain is severe, persistent, or radiates down one or both legs, or if there is numbness or weakness.",
        "Drug Recommendations": ["Ibuprofen", "Acetaminophen", "Muscle relaxants", "Gabapentin"]
    }
}

# Title Section
st.markdown("<h1 style='text-align: center; color: black;'>🌟 Medical Recommendation System</h1>", unsafe_allow_html=True)

# Medical Calculators Section
st.header("Medical Calculators")

# 1. BMI Calculator
st.subheader("1. Body Mass Index (BMI) Calculator")
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm)", min_value=50.0, step=0.1)

if weight > 0 and height > 0:
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("BMI Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("BMI Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("BMI Category: Overweight")
    else:
        st.write("BMI Category: Obesity")

# 2. Heart Rate Calculator
st.subheader("2. Heart Rate Target Zone Calculator")
age = st.number_input("Enter your age", min_value=1, step=1)
if age > 0:
    max_heart_rate = 220 - age
    target_heart_rate_60 = max_heart_rate * 0.6
    target_heart_rate_85 = max_heart_rate * 0.85
    st.write(f"Your target heart rate zone is between {target_heart_rate_60:.2f} and {target_heart_rate_85:.2f} beats per minute.")

# 3. Pregnancy Due Date Calculator
st.subheader("3. Pregnancy Due Date Calculator")
lmp_date = st.date_input("Enter the first day of your last menstrual period (LMP)")
if lmp_date:
    due_date = lmp_date + pd.DateOffset(days=280)  # Add 280 days (40 weeks)
    st.write(f"Your estimated due date is: {due_date.strftime('%B %d, %Y')}")

# 4. Ideal Weight Calculator
st.subheader("4. Ideal Weight Calculator")
gender = st.selectbox("Select your gender", ["Male", "Female"])
height_ft = st.number_input("Enter your height (in feet)", min_value=3.0, step=0.1)

if height_ft > 0:
    height_in_inches = (height_ft - 5) * 12  # Calculate height over 5 feet in inches
    if gender == "Male":
        ideal_weight = 48 + (2.7 * height_in_inches)
    else:
        ideal_weight = 45.5 + (2.2 * height_in_inches)

    st.write(f"Your ideal weight is: {ideal_weight:.2f} kg")

# Symptom-Based Recommendations Section
st.header("Symptom-Based Recommendations")

# Allow users to select a symptom from the dropdown menu
symptom = st.selectbox("Choose a symptom:", list(symptom_recommendations.keys()))

if symptom:
    recommendations = symptom_recommendations[symptom]
    
    st.write(f"### Recommendations for: {symptom}")
    st.write("#### Possible Conditions:")
    for condition in recommendations["Possible Conditions"]:
        st.write(f"- {condition}")
    
    st.write("#### General Remedy:")
    st.write(recommendations["General Remedy"])
    
    st.write("#### When to See a Doctor:")
    st.write(recommendations["When to See a Doctor"])
    
    # Display drug recommendations
    st.write("#### Recommended Drugs:")
    for drug in recommendations["Drug Recommendations"]:
        st.write(f"- {drug}")

# Drug Interactions Checker Section
st.header("Drug Interactions Checker")

# Define the list of drugs from the predefined data
drug_list = list(drug_data.keys())

# Allow users to select drugs from the dropdown menu
drug1 = st.selectbox("Select the first drug:", drug_list)
drug2 = st.selectbox("Select the second drug:", drug_list)

if drug1 and drug2:
    if drug1 == drug2:
        st.write("Please select two different drugs.")
    else:
        # Check for interactions between the selected drugs
        interactions = drug_data.get(drug1, []) + drug_data.get(drug2, [])
        interactions = set(interactions)  # Remove duplicate interactions

        # Display the results
        if len(interactions) > 0:
            st.write(f"Potential interactions between {drug1} and {drug2}:")
            for interaction in interactions:
                st.write(f"- {interaction}")
        else:
            st.write(f"No significant interactions found between {drug1} and {drug2}.")

# Disclaimer
st.sidebar.title("Disclaimer")
st.sidebar.write("""
This system provides general information and is not a substitute for professional medical advice, diagnosis, or treatment. 
Always consult your doctor or qualified healthcare provider for specific medical concerns.
""")



