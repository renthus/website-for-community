from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

user_list = ['Renato', 'Tatiana', 'Valentina']

app.config['SECRET_KEY'] = 'M8jk07jHGd18yDKJioPhsJWlMg'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', user_list=user_list)

@app.route("/login", methods=['GET','POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and 'submit_login' in request.form:
        flash(f'Login feito com sucesso para o e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criar_conta.validate_on_submit() and 'submit_criar_conta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)

if __name__ == '__main__':
    app.run(debug=True)