from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager
import bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = "your key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username = username, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso"})
    
    return jsonify({"message": "Dados invalidos"}), 400




if __name__ == '__main__':
    app.run(debug=True)