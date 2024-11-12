from flask import Blueprint, request, jsonify
from controller.diabetes_controller import DiabetesController

predict_routes = Blueprint('predict_routes', __name__)
diabetes_controller = DiabetesController(data_path=r"C:\Users\migue\OneDrive\Documentos\diabetesApi\diabetes_prediction_dataset.csv")

@predict_routes.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        gender = data.get('gender')
        age = data.get('age')
        hypertension = data.get('hypertension')
        heart_disease = data.get('heart_disease')
        smoking_history = data.get('smoking_history')
        bmi = data.get('bmi')
        hba1c_level = data.get('hba1c_level')
        blood_glucose_level = data.get('blood_glucose_level')

        prediction = diabetes_controller.predict_diabetes(
            gender, age, hypertension, heart_disease,
            smoking_history, bmi, hba1c_level, blood_glucose_level
        )

        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@predict_routes.route('/model/evaluation', methods=['GET'])
def model_evaluation():
    try:
        evaluation_report = diabetes_controller.get_evaluation_report()
        return jsonify(evaluation_report)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
