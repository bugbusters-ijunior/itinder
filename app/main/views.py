from flask import render_template, url_for, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login_manager
from app.main.models import User, Diretoria, Association
from app.main.forms import LoginForm, CadastroForm
from app.main.utils import encrypt, decrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and decrypt(user.senha) == form.senha.data:
            login_user(user)
            return redirect(url_for('choice'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))    

@app.route('/cadastro_trainee', methods = ['POST','GET'])
def cadastro_trainee():
    form = CadastroForm()
    
    if form.validate_on_submit():
        email = form.email.data
        nome = form.nome.data
        senha = encrypt(form.senha.data)

        user = User(email, nome, senha)
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('cadastrar_trainee.html', form=form)

@app.route('/perfil/<id>')
@login_required
def perfil(id):
    user = User.query.get_or_404(id)

    return render_template('perfil_trainee.html', trainee = user)

@app.route('/choice', methods=["POST","GET"])
@login_required
def choice():
    user = current_user
    diretorias = Diretoria.query.all()

    if request.method == 'POST':
        id_diretoria = request.form['id_diretoria']
        diretoria = Diretoria.query.get_or_404(id_diretoria)
        
        assoc = Association(user, diretoria)

        db.session.add(assoc)
        db.session.commit()


    return render_template('choice.html')
