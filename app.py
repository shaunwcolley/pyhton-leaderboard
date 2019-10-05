from flask import Flask, request
app = Flask(__name__)

data = [
{'id': 1, 'key': 'abc123', 'email': 'steve@steve.com'},
{'id': 2, 'key': 'def456', 'email': 'bill@steve.com'},
{'id': 3, 'key': 'ghi789', 'email': 'lisa@steve.com'},
]

keys = []

for item in data:
    keys.append(item['key'])



from functools import wraps

def home_decorator():
    def _home_decorator(f):
        @wraps(f)
        def __home_decorator(*args, **kwargs):
            # just do here everything what you need

            result = f(*args, **kwargs)

            key = 'False';
            index = 0
            check = True

            while check:
                if(result == keys[index]):
                    check = False
                    return result
                index += 1
                print(index)
                if(index >= len(keys)):
                    break
            return key

        return __home_decorator
    return _home_decorator

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

@app.route('/<key>/bill')
@home_decorator()
def home(key):
    return key
