Minha Aplicação Flask
Este é um simples guia para iniciar uma aplicação Flask com um ambiente virtual e um arquivo requirements.txt.

Configuração

Clonar o Repositório:
git clone https://github.com/seu-usuario/minha-aplicacao-flask.git
cd minha-aplicacao-flask

Configurar o Ambiente Virtual:
# Instalar, Criar, ativar o virtualenv (caso ainda não tenha)
pip install virtualenv
virtualenv venv
# Ativar o ambiente virtual (Windows)
venv\Scripts\activate
# Ativar o ambiente virtual (Unix ou MacOS)
source venv/bin/activate

Instalar Dependências:
pip install -r requirements.txt

python app.py
