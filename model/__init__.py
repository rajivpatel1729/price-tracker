from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ProductData(db.Model):
    link = db.Column(db.String(1000), nullable=False, primary_key=True)
    name = db.Column(
        db.String(50),
        nullable=False,
    )


class ProductInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(1000), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    price = db.Column(db.String(100), nullable=False)

class TrackingProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(1000), nullable=False)
