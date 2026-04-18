from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Final Project CI/CD Pipeline!"

@app.route('/service')
def service():
    return "SERVICERUNNING"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
