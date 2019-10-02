from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/user/<username>')
def show_user(username):
    return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post: ' + str(post_id)
