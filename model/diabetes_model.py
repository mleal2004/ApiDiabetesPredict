import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder


class DiabetesModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.clf = KNeighborsClassifier(n_neighbors=5)
        self.le_gender = LabelEncoder()
        self.le_smoking = LabelEncoder()
        self.entrenar_modelo()
        self.evaluation_report = None

    def entrenar_modelo(self):
        data = pd.read_csv(self.data_path)
        X = data.drop("diabetes", axis=1)
        y = data["diabetes"]

        X["gender"] = self.le_gender.fit_transform(X["gender"])
        X["smoking_history"] = self.le_smoking.fit_transform(X["smoking_history"])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42)
        
        self.clf.fit(X_train, y_train)
        y_pred = self.clf.predict(X_test)

        # Guardar la precisión y el reporte de clasificación
        self.evaluation_report = classification_report(y_test, y_pred, output_dict=True)
        print("Reporte de clasificación:\n", classification_report(y_test, y_pred))

    def predecir(self, caracteristicas):
        return self.clf.predict([caracteristicas])[0]

    def encode_features(self, gender, smoking_history):
        return (self.le_gender.transform([gender])[0],
                self.le_smoking.transform([smoking_history])[0])
    
    def obtener_reporte_evaluacion(self):
        data = pd.read_csv(self.data_path)
        X = data.drop("diabetes", axis=1)
        y = data["diabetes"]

        X["gender"] = self.le_gender.fit_transform(X["gender"])
        X["smoking_history"] = self.le_smoking.fit_transform(X["smoking_history"])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42)
        
        self.clf.fit(X_train, y_train)
        y_pred = self.clf.predict(X_test)

        # Guardar la precisión y el reporte de clasificación
        self.evaluation_report = classification_report(y_test, y_pred, output_dict=True)
        return self.evaluation_report
