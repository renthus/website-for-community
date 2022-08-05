from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from community.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha =PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmação da senha', validators=[DataRequired(), EqualTo('senha')])
    submit_criar_conta = SubmitField('Criar Conta')

    def validate_username(self, username):
        usuario_username = Usuario.query.filter_by(username=username.data).first()
        if usuario_username:
            raise ValidationError('Nome de usuário já cadastrado. Insira outro nome!')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar!')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar = BooleanField('Lembrar Dados de Acesso')
    submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    submit_perfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com este e-mail. Cadastre outro e-mail')

    def validate_username(self, username):
        if current_user.username != username.data:
            usuario = Usuario.query.filter_by(username=username.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com este username. Cadastre outro username')