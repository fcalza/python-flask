from flask import render_template, request, redirect, session, flash, url_for
from flask_bcrypt import check_password_hash

from app import app
from models import  Usuario
from helpers import FormularioUsuario


@app.route('/login')
def login():
    form = FormularioUsuario()
    return render_template('login.html', titulo='Login', form=form)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuario.query.filter_by(nickname=form.nickname.data).first()
    if not usuario:
        flash('Usuario nao localizado!')
        return redirect(url_for('login'))
    
    senha = check_password_hash(usuario.senha, form.senha.data)
    if senha:
        session['usuario_logado'] = usuario.senha
        flash('Login efetuado com sucesso! '+ usuario.nome)
        return redirect(url_for('inicio'))
    flash('Senha errada! '+ usuario.nome)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado!')
    return redirect(url_for('login'))
