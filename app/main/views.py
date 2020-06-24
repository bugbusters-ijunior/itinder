from flask import render_template
from app import app, db
from app.main.models import Trainee, Diretoria, Association

@app.route('/')
def teste():
    
    
    return render_template('teste.html')
