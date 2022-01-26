from app.extensions import db
from app.models import BaseModel

class User(BaseModel):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(70))
    email = db.Column(db.String(50), unique = True, index = True)
    cpf = db.Column(db.String(11), unique = True)
    tel = db.Column(db.String(11))
    password = db.Column(db.String(64))

    user_product = db.relationship("Produto", backref="user")

    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "tel": self.tel
        }
