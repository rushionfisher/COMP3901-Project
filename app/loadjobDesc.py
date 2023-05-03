import mysql.connector
import os

# Connect to the database
db_config = {
    'user': 'capstone',
    'password': 'Password876!@#',
    'host': 'localhost',
    'database': 'uwicareers',
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Create directory for job description files
if not os.path.exists('job_desc_files'):
    os.makedirs('job_desc_files')

# Fetch all columns from the jobs table
cursor.execute('SELECT * FROM `jobs`')
data = cursor.fetchall()

# Write job description data to individual files
for row in data:
    job_id = str(row[0])
    job_desc = str(row).strip()

    file_name = f"{job_id}.txt"
    file_path = os.path.join('job_desc_files', file_name)

    with open(file_path, 'w+') as f:
        f.write(job_desc)