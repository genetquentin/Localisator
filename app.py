from flask import Flask, render_template, request, url_for, redirect, session
import os
from functools import wraps

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
