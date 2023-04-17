from flask import Flask, render_template, request, session, redirect
import mysql.connector
from datetime import timedelta
import bcrypt

app = Flask(__name__)
app.secret_key = '1q2w3e4r5t'
app.permanent_session_lifetime = timedelta(days=7)

## MySQL database configuration
db_config = {
    'user': 'capstone',
    'password': 'Password876!@#',
    'host': 'localhost',
    'database': 'uwicareers',
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor(prepared=True)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html')


@app.route('/check')
def checklogin():
    if 'username' in session:
        return 'You are already logged in as ' + session['username']
    else:
        return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['ID']
        password = request.form['password']
        remember_me = request.form.get('remember')

        # Validate input
        if not username or not password:
            error = 'Username and password are required'
            return render_template('login.html', error=error)

        # Retrieve user data from database
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        data = cursor.fetchone()

        if not data:
            error = 'Invalid login'
            return render_template('login.html', error=error)

        # Check password
        stored_hash = data[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            # Login successful
            session['username'] = username
            if remember_me:
                session.permanent = True  
            message = "Login Successful"
            return render_template('login.html', message=message)
        else:
            # Login unsuccessful
            error = 'Invalid login'
            return render_template('login.html', error=error)

    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()
