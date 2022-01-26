from app.produto.model import Produto
from flask import request, jsonify
from flask.views import MethodView
from datetime import datetime

class ProdutoG(MethodView):
    
    def post(self):
        body = request.json

        cod = body.get("codigo")
        preco = body.get("preco")
        pedido = body.get("pedido")

        if isinstance(cod, str) and isinstance(preco, float) and isinstance(pedido, bool):
            produto = Produto(cod=cod, preco=preco, pedido=pedido)
            produto.save()
            return produto.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def get(self):

        produtos = Produto.query.all()
        return jsonify([produto.json() for produto in produtos]), 200


class ProdutoId(MethodView):

    def get(self, id):
        produto = Produto.query.get_or_404(id)
        return produto.json()

    
    def put(self, id):
        body = request.json

        cod = body.get("codigo")
        preco = body.get("preco")
        pedido = body.get("pedido")
        user_id = body.get("user_id")

        if isinstance(cod, str) and isinstance(preco, float) and isinstance(pedido, bool) and (isinstance(user_id, int) or user_id == None):
            produto = Produto.query.get_or_404(id)
            produto.cod = cod
            produto.preco = preco
            produto.pedido = pedido
            produto.user_id = user_id
            produto.update()
            return produto.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def patch(self, id):
        body = request.json

        cod = body.get("codigo", self.cod)
        preco = body.get("preco", self.preco)
        pedido = body.get("pedido", self.pedido)
        user_id = body.get("user_id", self.user_id)

        if isinstance(cod, str) and isinstance(preco, float) and isinstance(pedido, bool) and (isinstance(user_id, int) or user_id == None):
            produto = Produto.query.get_or_404(id)
            produto.cod = cod
            produto.preco = preco
            produto.pedido = pedido
            produto.user_id = user_id
            produto.update()
            return produto.json(), 200
        return {"code_status": "Invalid data in request"}, 400


    def delete(self, id):
        produto = Produto.query.get_or_404(id)
        produto.delete(produto)
        return {"code_status": "deleted"}, 200
