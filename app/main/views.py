from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login_manager
from app.main.models import Trainee, Diretoria, Association
from app.main.forms import LoginForm, CadastroForm

@login_manager.user_loader
def load_user(user_id):
    return Trainee.query.filter_by(id=user_id).first()

@app.route('/')
@login_required
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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))    

@app.route('/like_diretoria', methods=['POST','GET'])
def like_diretoria():
    trainee = current_user
    diretorias = Diretoria.query.all()

    if request.method == 'POST':
        id_diretoria = request.form['id_diretoria']
        diretoria = Diretoria.query.get_or_404(id_diretoria)
        
        assoc = Association(trainee, diretoria)

        db.session.add(assoc)
        db.session.commit()

        return redirect(url_for('app.index'))

    return render_template('like_diretoria.html', diretoria = diretorias)

@app.route('/cadastro_trainee', methods = ['POST','GET'])
def cadastro_trainee():
    form = CadastroForm()
    
    if form.validate_on_submit():
        email = form.email.data
        nome = form.nome.data
        senha = form.senha.data

        trainee = Trainee(email, nome, senha)
        
        db.session.add(trainee)
        db.session.commit()

        return redirect(url_for(app.index))
    return render_template('cadastrar_trainee.html')

@app.route('/perfil/<id>')
def perfil(id):
    trainee = Trainee.query.get_or_404(id)

    return render_template('perfil_trainee.html', trainee = trainee)

@app.route('/choice')
def choice():

    return render_template('choice.html')
