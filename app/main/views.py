from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user
from app import app, db, login_manager
from app.main.models import Trainee, Diretoria, Association
from app.main.forms import LoginForm

@login_manager.user_loader
def load_user(user_id):
    return Trainee.query.filter_by(id=user_id).first()

@app.route('/')
def teste():
    return render_template('teste.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        trainee = Trainee.query.filter_by(email=form.email.data).first()
        if trainee and trainee.senha == form.senha.data:
            login_user(trainee)
            return redirect(url_for('teste'))

    return render_template('login.html', form=form)    
