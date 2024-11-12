from model.diabetes_model import DiabetesModel

class DiabetesController:
    def __init__(self, data_path):
        self.model = DiabetesModel(data_path)

    def predict_diabetes(self, gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level):
        gender_encoded, smoking_encoded = self.model.encode_features(gender, smoking_history)
        features = [
            gender_encoded, age, hypertension, heart_disease,
            smoking_encoded, bmi, hba1c_level, blood_glucose_level
        ]
        return self.model.predecir(features)
    
    def get_evaluation_report(self):
        return self.model.obtener_reporte_evaluacion()

