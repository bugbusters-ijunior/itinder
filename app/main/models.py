from app import db

class Trainee(db.Model):
    __tablename__ = 'trainees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    senha = db.Column(db.String)

    diretorias = db.relationship("Association", back_populates="trainee")

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
        return '<Trainee %r>' % self.nome


class Diretoria(db.Model):
    __tablename__ = 'diretorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    diretor = db.Column(db.String, unique=True)

    trainees = db.relationship("Association", back_populates="diretoria")

    def __init__(self, nome, diretor):
        self.nome = nome
        self.diretor = diretor

    def __repr__(self):
        return '<Diretoria %r>' % self.nome


class Association(db.Model):
    __tablename__ = 'association'
    
    trainee_id = db.Column(db.Integer, db.ForeignKey('trainees.id'), primary_key=True)
    diretoria_id = db.Column(db.Integer, db.ForeignKey('diretorias.id'), primary_key=True)
    trainee = db.relationship("Trainee", back_populates="diretorias")
    diretoria = db.relationship("Diretoria", back_populates="trainees")

    def __init__(self, trainee, diretoria):
        self.trainee = trainee
        self.diretoria = diretoria
    