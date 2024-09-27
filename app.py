import time
import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory

app = Flask(__name__)
app.secret_key = os.urandom(24)


# setting up the main route to render the index.html template - donskyblock 9/28/24
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Custom error handler for 404 errors - donskyblock - 9/28/24
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  