from app.user.model import User
from flask import request, jsonify
from flask.views import MethodView

class UserG(MethodView):
    
    def post(self):
        body = request.json

        nome = body.get("nome")
        email = body.get("email")
        cpf = body.get("cpf")
        tel = body.get("tel")
        password = body.get("password")

        if isinstance(nome, str) and isinstance(email, str) and isinstance(cpf, str) and isinstance(tel, str) and isinstance(password, str):
            user = User(nome=nome, email=email, cpf=cpf, tel=tel, password=password)
            user.save()
            return user.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def get(self):

        users = User.query.all()
        return jsonify([user.json() for user in users]), 200


class UserId(MethodView):

    def get(self, id):
        user = User.query.get_or_404(id)
        return user.json()

    
    def put(self, id):
        body = request.json

        nome = body.get("nome")
        email = body.get("email")
        cpf = body.get("cpf")
        tel = body.get("tel")
        password = body.get("password")

        if isinstance(nome, str) and isinstance(email, str) and isinstance(cpf, str) and isinstance(tel, str) and isinstance(password, str):
            user = User.query.get_or_404(id)
            user.nome = nome
            user.email = email
            user.cpf = cpf
            user.tel = tel
            user.password = password
            user.update()
            return user.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def patch(self, id):
        body = request.json

        user = User.query.get_or_404(id)

        nome = body.get("name", user.nome)
        email = body.get("email", user.email)
        cpf = body.get("cpf", user.cpf)
        tel = body.get("tel", user.tel)
        password = body.get("password", user.password)

        if isinstance(nome, str) and isinstance(email, str) and isinstance(cpf, str) and isinstance(tel, str) and isinstance(password, str):
            user.nome = nome
            user.email = email
            user.cpf = cpf
            user.tel = tel
            user.password = password
            user.update()
            return user.json(), 200
        return {"code_status": "Invalid data in request"}, 400


    def delete(self, id):
        user = User.query.get_or_404(id)
        user.delete(user)
        return {"code_status": "deleted"}, 200
