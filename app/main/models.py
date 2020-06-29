from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    senha = db.Column(db.String)

    diretorias = db.relationship("Association", back_populates="user")

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, email, nome, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return '<User %r>' % self.nome


class Diretoria(db.Model):
    __tablename__ = 'diretorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    diretor = db.Column(db.String, unique=True)
    descricao = db.Column(db.String)
    ref_imagem = db.Column(db.String)

    users = db.relationship("Association", back_populates="diretoria")

    def __repr__(self):
        return '<Diretoria %r>' % self.nome


class Association(db.Model):
    __tablename__ = 'association'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    diretoria_id = db.Column(db.Integer, db.ForeignKey('diretorias.id'), primary_key=True)
    user = db.relationship("User", back_populates="diretorias")
    diretoria = db.relationship("Diretoria", back_populates="users")

    def __init__(self, user, diretoria):
        self.user = user
        self.diretoria = diretoria
    