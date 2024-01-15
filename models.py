from app import db


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    categoria = db.Column(db.String(40))
    console = db.Column(db.String(20))

    def __init__(self, nome, categoria, console, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
    def __repr__(self):
        return '<Jogo %r>' % self.nome
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20))
    nickname = db.Column(db.String(20))
    senha = db.Column(db.String(100))

    def __init__(self, nome, nickname, senha, id=None):
        self.id = id
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
    
    def __repr__(self):
        return '<Usuario %r>' % self.nome
