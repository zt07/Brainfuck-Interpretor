from flask import Flask, request, render_template, Blueprint
import brainfuck
from brainfuckery import Brainfuckery
app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')


@app.route('/interpret', methods=['POST'])
def interpret():
    if request.method == 'POST':
        code = request.form['in']
        result = brainfuck.evaluate(code)
        return render_template('index.html', result=result)

@app.route('/Translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        code = request.form['Translate']
        result = Brainfuckery().convert(code)
        return render_template('index.html', result=result)

if __name__=='__main__':
    app.run(debug=True)
