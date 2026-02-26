DATASET1_SCHEMA_RENAME = {
    "Patient_Number": "patient_number",
    "Blood_Pressure_Abnormality": "blood_pressure_abnormality",
    "Level_of_Hemoglobin": "level_of_hemoglobin",
    "Genetic_Pedigree_Coefficient": "genetic_pedigree_coefficient",
    "Age": "age",
    "BMI": "bmi",
    "Sex": "sex",
    "Pregnancy": "pregnancy",
    "Smoking": "smoking",
    "Level_of_Stress": "level_of_stress",
    "Chronic_kidney_disease": "chronic_kidney_disease",
    "Adrenal_and_thyroid_disorders": "adrenal_thyroid_disorders"
}

DATASET2_SCHEMA_RENAME = {
    "Patient_Number": "patient_number",
    "Day_Number": "day_number",
    "Physical_activity": "physical_activity_steps_per_day"
}

DATASET1_SCHEMA = {
    "patient_number": {},
    "sex": {"values": {0: "Male", 1: "Female"}},
    "smoking": {"values": {0: "No", 1: "Yes"}},
    "chronic_kidney_disease": {"values": {0: "No", 1: "Yes"}},
    "blood_pressure_abnormality": {"values": {0: "Normal", 1: "Abnormal"}},
    "age": {},
    "bmi": {},
    "level_of_stress": {"values": {1: "Low", 2: "Normal", 3: "High"}},
    "primary_key":["patient_number"]
}

DATASET2_SCHEMA = {
    "patient_number": {},
    "day_number": {},
    "physical_activity_steps_per_day": {},
    "foreign_key": ["patient_number"]
}

RELATIONSHIP = {
    "join_key": "patient_number"
}