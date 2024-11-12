from flask import Flask
from flask_cors import CORS
from view.predict_routes import predict_routes
from view.user_view import user_bp
from config import db, Config, init_app

app = Flask(__name__)
app.config.from_object(Config)

init_app(app)

app.register_blueprint(predict_routes)
app.register_blueprint(user_bp)

CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == "__main__":
    app.run(debug=True)
