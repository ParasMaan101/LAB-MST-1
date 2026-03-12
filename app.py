from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if len(password) < 6:
        return "Password must be at least 6 digits"

    if email == "admin@gmail.com" and password == "123456":
        return "Login Successful"
    else:
        return "Invalid Email or Password"

if __name__ == '__main__':
    app.run(debug=True)