from app.extensions import db
from app.models import BaseModel
from datetime import datetime

class Produto(BaseModel):

    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cod = db.Column(db.String, unique=True)
    preco = db.Column(db.Float)
    fabricacao = db.Column(db.DateTime, default=datetime.utcnow)
    pedido = db.Column(db.Boolean, default = False)

    user_id = db.Column(db.ForeignKey("user.id"))

    def json(self):
        return {
            "code": self.cod,
            "preco": self.preco,
            "fabricacao": self.fabricacao,
            "pedido": self.pedido,
            "user": self.user_id
        }

