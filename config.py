import os

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/jogoteca'
SECRET_KEY = 'senha_do_banco'
UPLOAD_PATH = os.path.dirname(__file__) + '/arquivos'