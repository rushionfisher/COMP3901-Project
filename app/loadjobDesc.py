import mysql.connector

#connect to the database
db_config = {
    'user': 'capstone',
    'password': 'Password876!@#',
    'host': 'localhost',
    'database': 'uwicareers',
}

# Connect to the database
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

#Fetch job description data from database
cursor.execute('SELECT jobDescription FROM `jobs`')
data = cursor.fetchall()

# Open jobDescription file and write data from the database to it
with open('jobDesc.txt', 'w+') as f:
    for row in data:
        f.write(str(row).strip('(').strip(')').strip(',') + '\n')