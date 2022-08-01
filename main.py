from flask import Flask, render_template

app = Flask(__name__)

user_list = ['Renato', 'Tatiana', 'Valentina']

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', user_list=user_list)

if __name__ == '__main__':
    app.run(debug=True)