# -*- coding: UTF-8 -*-
"""
lynda.com flask essential training 
"""
from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify  # From module flask import class Flask
import json
import os.path
from werkzeug.utils import secure_filename
from fileinput import filename

app = Flask(__name__)    # Construct an instance of Flask class for our webapp
app.secret_key = "longsecurekey"

@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')
    


if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)  # Enable reloader and debugger