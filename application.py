
from flask import Flask, request
import requests

application = Flask(__name__)

@application.route('/')
def index():
    url = request.args.get('url')
    response = requests.get(url)
    # use the parameters in your code
    return response.content

if __name__ == '__main__':
    application.run(debug=True)
    