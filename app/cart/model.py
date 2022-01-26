from app.extensions import db
from app.models import BaseModel

class Cart(BaseModel):

    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    user_id = db.Column(db.ForeignKey("user.id"))
    prod = db.relationship("Produto", backref="cart")

    def json(self):
        return {
            "user_id": self.user_id
        }