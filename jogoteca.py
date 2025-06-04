from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
    def __str__(self):
        return f"{self.nome} ({self.categoria} - {self.console})"

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Crash', 'Corrida', 'PS2')
lista = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    lista.append(Jogo(nome, categoria, console))
    return redirect('/')

app.run(host='0.0.0.0', port=5000, debug=True)