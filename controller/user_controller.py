from model.user_model import User

class UserController:
    
    @staticmethod
    def register_user(username, password):
        if User.find_by_username(username):
            return {"msg": "Usuario ya existe"}, 400

        new_user = User(username=username, password=password)
        new_user.save()
        return {"msg": "Usuario registrado exitosamente"}, 200

    @staticmethod
    def authenticate_user(username, password):
        user = User.find_by_username(username)
        if user and user.check_password(password):
            return user
        return None
