from flask import Flask, url_for, request, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def lindex():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

    