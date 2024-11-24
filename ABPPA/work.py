from flask import Flask, url_for, request, render_template, redirect

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
    
    return render_template('login.html')

FRUIT_MANUFACTURER_DATABASE = {
    "apple": ["Apple Orchard Inc.", "Tropical Banana Farms"],
    "banana": ["Tropical Banana Farms", "Dairy Delight Ltd."],
    "carrot": ["Fresh Veggie Co."],
    "milk": ["Dairy Delight Ltd."],}

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    product_info = None
    manufacturer_info = None
    manufacturers_of_fruit = None
    if request.method == 'POST':
        product_name = request.form['product_name'].lower()
        if product_name in FRUIT_MANUFACTURER_DATABASE:
            manufacturers_of_fruit = FRUIT_MANUFACTURER_DATABASE.get(product_name)
            product_info = f"{product_name.capitalize()} is produced by the following manufacturers:"
        else:
            product_info = "Product not found."

    return render_template('dashboard.html', product_info=product_info, manufacturers_of_fruit=manufacturers_of_fruit)


if __name__ == '__main__':
    app.run(debug=True)

    