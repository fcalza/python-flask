import os
from flask import flash, session

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators

from app import app


class FormularioJogo(FlaskForm):
    nome = StringField('Nome do jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=20)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')



def valida_session():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Faça o login antes de acessar essa página!')
        return False
    return True


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.png'


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))

