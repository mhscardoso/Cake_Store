from app.produto.model import Produto
from flask import request, jsonify
from flask.views import MethodView
from datetime import datetime

class ProdutoG(MethodView):
    
    def post(self):
        body = request.json

        nome = body.get("nome")
        sabor = body.get("sabor")
        cod = body.get("codigo")
        preco = body.get("preco")
        pedido = body.get("pedido")

        prod = Produto.query.filter_by(cod=cod).first()
        if prod:
            return {"code_status": "Product already in"}, 400

        if isinstance(cod, str) and isinstance(preco, float) and isinstance(pedido, bool) and isinstance(nome, str) and isinstance(sabor, str):
            produto = Produto(cod=cod, preco=preco, pedido=pedido, nome=nome, sabor=sabor)
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

        nome = body.get("nome")
        sabor = body.get("sabor")
        cod = body.get("codigo")
        preco = body.get("preco")
        pedido = body.get("pedido")
        cart_id = body.get("cart_id")

        prod = Produto.query.filter_by(cod=cod).first()
        if prod:
            return {"code_status": "Product already in"}, 400

        if isinstance(cod, str) and isinstance(preco, float) and isinstance(pedido, bool) and (isinstance(cart_id, int) or cart_id == None) and isinstance(nome, str) and isinstance(sabor, str):
            produto = Produto.query.get_or_404(id)
            produto.cod = cod
            produto.preco = preco
            produto.pedido = pedido
            produto.user_id = cart_id
            produto.nome = nome
            produto.sabor = sabor
            produto.update()
            return produto.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def patch(self, id):
        body = request.json

        nome = body.get("nome", self.nome)
        sabor = body.get("sabor", self.sabor)
        cod = body.get("codigo", self.cod)
        preco = body.get("preco", self.preco)
        pedido = body.get("pedido", self.pedido)
        cart_id = body.get("cart_id", self.cart_id)

        if isinstance(cod, str) and isinstance(preco, float) and isinstance(pedido, bool) and (isinstance(cart_id, int) or cart_id == None) and isinstance(nome, str) and isinstance(sabor, str):
            produto = Produto.query.get_or_404(id)
            produto.cod = cod
            produto.preco = preco
            produto.pedido = pedido
            produto.user_id = cart_id
            produto.nome = nome
            produto.sabor = sabor
            produto.update()
            return produto.json(), 200
        return {"code_status": "Invalid data in request"}, 400


    def delete(self, id):
        produto = Produto.query.get_or_404(id)
        produto.delete(produto)
        return {"code_status": "deleted"}, 200
