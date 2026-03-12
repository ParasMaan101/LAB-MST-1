from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    # Simple validation (example)
    if email == "admin@example.com" and password == "12345":
        return "Login Successful"
    else:
        return "Invalid Email or Password"

if __name__ == '__main__':
    app.run(debug=True)