from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://usprr21gu9n9sqbi:4BvKMm0h0CbhlqLJeLTD@bx3imosxpdwsymvwhecx-mysql.services.clever-cloud.com:3306/bx3imosxpdwsymvwhecx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret-key'

def init_app(app):
    db.init_app(app)
    JWTManager(app)
