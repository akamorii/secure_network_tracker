from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/about')
def about_page():
    return 'about'


@app.route('/user/<string:name>/<int:iden>')
def user_info(name, iden):
    a = f'user_name: {name} user_id: {str(iden)}'
    return a


if __name__ == '__main__':
    app.run(debug=True)