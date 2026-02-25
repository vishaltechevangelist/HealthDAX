import json

DATASET1_SCHEMA = {
    "patient_number": {},
    "sex": {"values": {0: "Male", 1: "Female"}},
    "smoking": {"values": {0: "No", 1: "Yes"}},
    "chronic_kidney_disease": {"values": {0: "No", 1: "Yes"}},
    "blood_pressure_abnormality": {"values": {0: "Normal", 1: "Abnormal"}},
    "age": {},
    "bmi": {},
    "level_of_stress": {"values": {1: "Low", 2: "Normal", 3: "High"}},
}

DATASET2_SCHEMA = {
    "patient_number": {},
    "day_number": {},
    "physical_activity_steps_per_day": {}
}

RELATIONSHIP = {
    "join_key": "patient_number"
}