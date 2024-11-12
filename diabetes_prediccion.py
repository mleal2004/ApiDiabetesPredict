import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder


class DiabetesModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.clf = DecisionTreeClassifier(max_depth=3)
        self.le_gender = LabelEncoder()
        self.le_smoking = LabelEncoder()
        self.entrenar_modelo()

    def entrenar_modelo(self):
        # Cargar dataset
        data = pd.read_csv(self.data_path)

        # Separar características y etiquetas
        X = data.drop("diabetes", axis=1)
        y = data["diabetes"]

        # Convertir características categóricas a numéricas
        X["gender"] = self.le_gender.fit_transform(X["gender"])
        X["smoking_history"] = self.le_smoking.fit_transform(
            X["smoking_history"])

        # Dividir el dataset en datos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42)

        # Entrenar el modelo
        self.clf.fit(X_train, y_train)

        # Evaluar el modelo
        y_pred = self.clf.predict(X_test)
        print("Precisión:", accuracy_score(y_test, y_pred))
        print("Reporte de clasificación:\n",
              classification_report(y_test, y_pred))

    def predecir(self, caracteristicas):
        return self.clf.predict([caracteristicas])[0]

    def solicitar_datos_usuario(self):
        # Solicitar los datos del usuario
        gender = input("Género (Male/Female): ")
        age = float(input("Edad: "))
        hypertension = int(input("Hipertensión (0: No, 1: Sí): "))
        heart_disease = int(input("Enfermedad cardíaca (0: No, 1: Sí): "))
        smoking_history = input(
            "Historial de tabaquismo (never, former, current, No Info): ")
        bmi = float(input("IMC: "))
        hba1c_level = float(input("Nivel de HbA1c: "))
        blood_glucose_level = float(input("Nivel de glucosa en sangre: "))

        # Convertir valores categóricos a numéricos
        gender_encoded = self.le_gender.transform([gender])[0]
        smoking_encoded = self.le_smoking.transform([smoking_history])[0]

        # Crear el arreglo de características
        caracteristicas = [gender_encoded, age, hypertension, heart_disease,
                           smoking_encoded, bmi, hba1c_level, blood_glucose_level]

        # Realizar la predicción
        resultado = self.predecir(caracteristicas)
        print("Predicción (0: No diabetes, 1: Diabetes):", resultado)


# Uso
model = DiabetesModel(
    r"C:\Users\migue\OneDrive\Documentos\diabetesApi\diabetes_prediction_dataset.csv")
model.solicitar_datos_usuario()
