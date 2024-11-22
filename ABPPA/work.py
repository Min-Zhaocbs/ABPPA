from flask import Flask, url_for, request, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)