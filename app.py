from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/log_score', methods=['GET','POST'])
def log_score():
    if request.method == 'POST':
        info = request.get_json()
        print(info['initials'])
        print(info['score'])
        return 'post'
    elif request.method == 'GET':
        return 'get'
