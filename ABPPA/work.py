from flask import Flask, url_for, request, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('Index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == username and password == password:
            return redirect(url_for('dashboard'))
    
    return render_template('contact.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    product_info = None
    manufacturer_info = None
    manufacturers_of_fruit = None
    if request.method == 'POST':
        product_name = request.form['product_name'].lower()
    
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)

    