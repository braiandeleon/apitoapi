
from flask import Flask, request


application = Flask(__name__)

@application.route('/')
def index():

    # use the parameters in your code
    return 'hola'

if __name__ == '__main__':
    application.run(debug=True)
    