#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return '''index page!
            <a href=\'/signin\'>SignIn</a>'''

@app.route('/signin', methods=['GET'])
def sign_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="username"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return 'Hello, admin!'
    return 'Bad username or password!'

if __name__ == '__main__':
    app.run()