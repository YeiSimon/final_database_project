import psycopg2
from psycopg2 import sql

# Database connection parameters
db_config = {
        "dbname": "clinic_db",
        "user": "clinic_user",
        "password": "clinic_password",
        "host": "localhost",  # e.g., "localhost"
        "port": "5432"  # PostgreSQL 預設端口
    }

# Sample data
nurses = [
    ('Alice Johnson', '123-456-7890', 'alice.johnson@example.com', 'Pediatrics', 'LN12345'),
    ('Bob Smith', '234-567-8901', 'bob.smith@example.com', 'Emergency', 'LN23456'),
    ('Catherine Lee', '345-678-9012', 'catherine.lee@example.com', 'Oncology', 'LN34567'),
    ('David Brown', '456-789-0123', 'david.brown@example.com', 'Cardiology', 'LN45678'),
    ('Emma Davis', '567-890-1234', 'emma.davis@example.com', 'Neurology', 'LN56789')
]

try:
    # Connect to the database
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    # Insert query
    insert_query = """
    INSERT INTO nurses (name, phone, email, department, license_number)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Execute the query for each nurse
    cursor.executemany(insert_query, nurses)

    # Commit changes
    connection.commit()
    print("Records inserted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
