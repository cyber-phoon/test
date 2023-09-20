from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Guest')
    message = request.args.get('message', 'Привет!')
    return f'Hello {name}!\n{message}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)