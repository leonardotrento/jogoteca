from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Crash', 'Corrida', 'PS2')
lista = [jogo1, jogo2]

class Usuarios:
    def __init__(self, nome, apelido, senha):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        
usuario1 = Usuarios("Luiz Gustavo", "Luizinho", "Luiz123")
usuario2 = Usuarios("Leonardo Trento", "Leo", "Leo123")
usuario3 = Usuarios("Pedro Valentin", "Tin", "pedro123")

usuarios = {usuario1.apelido : usuario1,
            usuario2.apelido : usuario2,
            usuario3.apelido : usuario3}

app = Flask(__name__)
app.secret_key = 'projeto'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticador():
    usuario_form = request.form['usuario']
    senha_form = request.form['senha']
    proxima_pagina = request.form.get('proxima', url_for('index'))
    
    if usuario_form in usuarios:
        usuario = usuarios[usuario_form]
        if senha_form == usuario.senha:
            session['usuario_logado'] = usuario.apelido
            flash(f'{usuario.apelido} logado com sucesso')
            return redirect(proxima_pagina)
        else:
            flash('Senha incorreta')
            return redirect(url_for('login'))
    else:
        flash('Usuário não encontrado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)