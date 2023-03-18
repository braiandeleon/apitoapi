#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:55:10 2023

@author: braiandeleon
"""

from flask import Flask, request


application = Flask(__name__)

@application.route('/')
def index():
    url = request.args.get('url')
    param2 = request.args.get('param2')
    # use the parameters in your code
    response = request.get(url)
    # Print the content of the response
    return 'Hello World!'

if __name__ == '__main__':
    application.run(debug=True)