from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Hello World! con el pipeline del 2021 con mucha alegria y probando notificación 2.0'

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=80, debug = True)