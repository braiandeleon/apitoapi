#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:55:10 2023

@author: braiandeleon
"""

from flask import Flask, request
import requests


app = Flask(__name__)

@app.route('/endpoint')
def my_endpoint():
    url = request.args.get('param1')
    param2 = request.args.get('param2')
    # use the parameters in your code
    response = requests.get(url)
    # Print the content of the response
    return response.content