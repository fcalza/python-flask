from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from app import app, db
from models import Jogos, Usuario
import time

from helpers import FormularioJogo, recupera_imagem, deleta_arquivo, FormularioUsuario, valida_session


@app.route("/")
def inicio():
    valida_session()
    lista = Jogos.query.order_by(Jogos.id).all()
    return render_template("lista.html", titulo="Jogos", jogos=lista)


@app.route('/novo')
def novo():
    if not valida_session():
        return redirect(url_for('login'))
    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo', form=form)


@app.route('/criar', methods=['POST',])
def criar():
    if not valida_session():
        return redirect(url_for('login'))
    
    form = FormularioJogo(request.form)
    if not form.validate():
        return redirect(url_for('novo'))
    
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    jogo = Jogos(nome, categoria, console)
    
    jogo = Jogos.query.filter_by(nome=jogo.nome).first()
    if jogo:
        flash('Jogo já cadastrado!')
        return redirect(url_for('novo'))
    
    novo_jogo = Jogos(nome, categoria, console)
    db.session.add(novo_jogo)
    db.session.commit()
    
    if request.files:
        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = int(time.time())
        arquivo.save(f'{upload_path}/capa_{novo_jogo.id}-{timestamp}.png')
    
    return redirect(url_for('inicio'))


@app.route('/editar/<int:id>')
def editar(id):
    if not valida_session():
        return redirect(url_for('login'))
    jogo = Jogos.query.filter_by(id=id).first()
    if not jogo:
        flash('Jogo não encontrado!')
        return redirect(url_for('lista'))
    capa_jogo = recupera_imagem(id)
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    
    return render_template('editar.html', titulo='Editando Jogo', id=jogo.id, capa_jogo=capa_jogo, form=form)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    if not valida_session():
        return redirect(url_for('login'))
    
    id = request.form.get('id')
    
    form = FormularioJogo(request.form)
    if form.validate():
        jogo = Jogos.query.filter_by(id=id).first()
        if not jogo:
            flash('Jogo não encontrado!')
            return redirect(url_for('novo'))
        
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data
        db.session.commit()
        
        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = int(time.time())
        arquivo.save(f'{upload_path}/capa_{jogo.id}-{timestamp}.png')

        deleta_arquivo(jogo.id)
    
    return redirect(url_for('inicio'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if not valida_session():
        return redirect(url_for('login'))
    print('passou')
    jogo = Jogos.query.filter_by(id=id).first()
    if not jogo:
        flash('Jogo não encontrado!')
        return redirect(url_for('inicio'))
    db.session.delete(jogo)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/arquivos/<nome_arquivo>')
def imagem(nome_arquivo):
    print(nome_arquivo)
    return send_from_directory('arquivos', nome_arquivo)