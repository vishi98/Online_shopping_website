import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopwala.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name

users = []

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         user = User(username=username, email=email, password=password)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("index"))
#     return render_template("register.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the user's information from the form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Create a new user object and add it to the list
        user = {'username': username, 'email': email, 'password': password}
        users.append(user)

        # Redirect the user to the login page
        return redirect('/login')

    return render_template('register.html')

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form['email']
#         password = request.form['password']
#         user = User.query.filter_by(email=email, password=password).first()
#         if user:
#             return redirect(url_for("dashboard"))
#         else:
#             return "Incorrect email or password. Please try again."
#     return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for("index"))
        else:
            return "Incorrect email or password. Please try again."
    return render_template("login.html")

# @app.route("/dashboard")
# def dashboard():
#     products = Product.query.all()
#     return render_template("dashboard.html", products=products)

@app.route("/buy/<int:id>", methods=["GET", "POST"])
def buy(id):
    product = Product.query.get(id)
    if request.method == "POST":
        # Implement real transaction here
        return "Transaction successful."
    return render_template("buy.html", product=product)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
