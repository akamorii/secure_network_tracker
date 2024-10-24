from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False )
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<article %r>' %self.id

@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:iden>')
def user_info(name, iden):
    a = f'user_name: {name} user_id: {str(iden)}'
    return a

@app.route('/login')
def login_page():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)