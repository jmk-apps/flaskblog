from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from flaskblog import db
from flaskblog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[InputRequired(), EqualTo("password", 'Passwords must match')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db.session.execute(db.select(User).where(User.username == username.data)).scalar()
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        user = db.session.execute(db.select(User).where(User.email == email.data)).scalar()
        if user:
            raise ValidationError("That email is taken. Please choose a different one.")


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = db.session.execute(db.select(User).where(User.username == username.data)).scalar()
            if user:
                raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = db.session.execute(db.select(User).where(User.email == email.data)).scalar()
            if user:
                raise ValidationError("That email is taken. Please choose a different one.")


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = TextAreaField('Content', validators=[InputRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = db.session.execute(db.select(User).where(User.email == email.data)).scalar()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first.")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[InputRequired(), EqualTo("password", 'Passwords must match')])
    submit = SubmitField('Reset Password')

