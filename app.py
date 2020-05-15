from flask import Flask, render_template, request, url_for, redirect, session
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geolocate')
def geolocate_page():
    return render_template('geolocate_page.html')



if __name__ == '__main__':
    app.run()
