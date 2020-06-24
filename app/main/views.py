from flask import render_template
from app import app

@app.route('/')
def teste():
    return render_template('teste.html')
