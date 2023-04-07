from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'capstone',
    'password': 'Password876!@#',
    'host': 'localhost',
    'database': 'jobListings',
}

# Connect to the database
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Define a route to display the content from the database on the webpage
@app.route('/joblisting.html', methods=['GET', 'POST'])
def joblisting():
    # Handle search form submission
    if request.method == 'POST':
        search_term = request.form['search']
        query = f"SELECT jobTitle, employer, DatePosted, status FROM jobs WHERE jobTitle LIKE '%{search_term}%'"
        cursor.execute(query)
        data = cursor.fetchall()
    else:
        # Execute a SELECT statement to retrieve all data from the database
        query = "SELECT jobTitle, employer, DatePosted, status FROM jobs"
        cursor.execute(query)
        data = cursor.fetchall()
    
    # Render the template and pass the data to the template
    return render_template('joblisting.html', data=data)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html')

@app.route('/about.html', methods=['GET'])
def aboutpage():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()


