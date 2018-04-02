from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, nome):
        self.nome = nome

class Venda(db.Model):
    __tablename__ = "venda"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    data = db.Column(db.String(20))
    vendedor = db.Column(db.String(50))

    cliente = db.relationship('Cliente', foreign_keys=cliente_id)

    def __init__(self, cliente_id, data, vendedor):
        self.cliente_id = cliente_id
        self.data = data
        self.vendedor = vendedor

class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80))
    preco = db.Column(db.Float)

    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco


@app.route("/")
def produtosMaisVendidos():
    return jsonify({"testejson": "teste"})

@app.route("/dados")
def dados():
    venda = Venda("3", "29/03/2018", "junior")
    db.session.add(venda)
    db.session.commit()
    return jsonify({"dataVenda:" : venda.data,
                    "vendedor:" :  venda.vendedor})


    if __name__ == "__main__":
        app.run(debug=True)
