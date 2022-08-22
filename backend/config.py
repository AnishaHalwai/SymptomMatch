import numpy as np
import pandas as pd

# list of all included diseases
diseases = np.array(['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
        'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes',
        'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',  'Migraine',
        'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
        'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
        'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
        'Dimorphic hemmorhoids(piles)', 'Heart attack','Varicose veins',
        'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
        'Osteoarthristis', 'Arthritis',
        '(vertigo) Paroymsal  Positional Vertigo','Acne',
        'Urinary tract infection','Psoriasis','Impetigo'])

def list_features():
        df = pd.read_csv("symptom_to_type.csv")
        list_of_features = list(df.columns)
        return list_of_features[:-1]

def symps_to_test(symptoms):
        all_feats = list_features()
        total_len = len(all_feats)
        test_data = np.zeros(total_len)

        for sy in symptoms:
                i = all_feats.index(sy)
                test_data[i] = 1

        return np.ndarray.tolist(test_data)


# print(symps_to_test(['itching', 'skin_rash', 'nodal_skin_eruptions','watering_from_eyes']))
