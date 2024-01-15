from time import sleep
import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print('Conectando...')

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE `jogoteca`;")
# conn.commit()

try:
    conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Nao possivel conectar. Usuario ou senha invalidos')
    else:
        print(err)

conn.cursor().execute('DROP DATABASE IF EXISTS jogoteca;')

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `jogoteca`;
    USE `jogoteca`;
    CREATE TABLE `jogos` (
      `id` SMALLINT NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `usuario` (
      `id` SMALLINT NOT NULL AUTO_INCREMENT,
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(20) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

sleep(3)

conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
cursor = conn.cursor()

# inserindo usuarios
cursor.executemany(
    'INSERT INTO jogoteca.usuario (nome, nickname, senha) VALUES (%s, %s, %s)',
    [
        ('teste1', 'teste1', generate_password_hash('123').decode('utf-8')),
        ('teste2', 'teste5', generate_password_hash('123').decode('utf-8')),
        ('teste3', 'teste4', generate_password_hash('123').decode('utf-8'))
    ]
)

cursor.execute('select * from jogoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
    'INSERT INTO jogoteca.jogos (nome, categoria, console) VALUES (%s, %s, %s)',
    [
        ('God of War 4', 'Ação', 'PS4'),
        ('NBA 2k18', 'Esporte', 'Xbox One'),
        ('Rayman Legends', 'Indie', 'PS4'),
        ('Super Mario RPG', 'RPG', 'SNES'),
        ('Super Mario Kart', 'Corrida', 'SNES'),
        ('Fire Emblem Echoes', 'Estratégia', '3DS'),
    ]
)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()


# mysql -u root -p
# show databases
# use jogoteca
# select + from jogos