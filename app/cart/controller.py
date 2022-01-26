from app.cart.model import Cart
from flask import request, jsonify
from flask.views import MethodView
from datetime import datetime

class CartG(MethodView):
    
    def post(self):
        body = request.json

        user_id = body.get("user")

        cart = Cart.query.filter_by(user_id=user_id).first()
        if cart:
            return {"code_status": "Cart already in"}, 400

        if isinstance(user_id, int):
            cart = Cart(user_id = user_id)
            cart.save()
            return cart.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def get(self):

        cart = Cart.query.all()
        return jsonify([cart.json() for cart in cart]), 200


class CartId(MethodView):

    def get(self, id):
        cart = Cart.query.get_or_404(id)
        return cart.json()

    
    def put(self, id):
        body = request.json

        user_id = body.get("user")

        cart2 = Cart.query.filter_by(user_id=user_id).first()
        if cart2.id != id:
            return {"code_status": "Cart already in"}, 400

        if isinstance(user_id, int):
            cart = Cart.query.get_or_404(id)            
            cart.user_id = user_id
            cart.update()
            return cart.json(), 200
        return {"code_status": "Invalid data in request"}, 400
    

    def patch(self, id):
        body = request.json

        user_id = body.get("user", self.user_id)

        cart2 = Cart.query.filter_by(user_id=user_id).first()
        if cart2.id != id:
            return {"code_status": "Cart already in"}, 400


        if isinstance(user_id, int):
            cart = Cart.query.get_or_404(id)
            cart.user_id = user_id
            cart.update()
            return cart.json(), 200
        return {"code_status": "Invalid data in request"}, 400


    def delete(self, id):
        cart = Cart.query.get_or_404(id)
        cart.delete(cart)
        return {"code_status": "deleted"}, 200
