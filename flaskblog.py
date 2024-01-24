from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
import os


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI")
db.init_app(app)


# Database models

# User model
class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    image_file: Mapped[str] = mapped_column(String(20), nullable=False, default="default.jpg")
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"User(username={self.username!r}, email={self.email!r}, image_file={self.image_file!r})"


# Post model
class Post(db.Model):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    date_posted: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    author: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self) -> str:
        return f"Post(title={self.title!r}, date_posted={self.date_posted!r})"


with app.app_context():
    db.create_all()

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run()
