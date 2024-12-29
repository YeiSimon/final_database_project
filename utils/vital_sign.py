from utils import load_data
import psycopg2

# Database configuration
db_config = {
    "dbname": "clinic_db",
    "user": "clinic_user",
    "password": "clinic_password",
    "host": "localhost",  # e.g., "localhost"
    "port": "5432"  # PostgreSQL default port
}

# Function to insert data into vital_signs table
def insert_vital_signs_data(data, db_config):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        cursor = conn.cursor()

        # Insert each record into the vital_signs table
        for record in data:
            cursor.execute("""
                INSERT INTO vital_signs (
                    appointment_id, nurse_id, temperature, blood_pressure, pulse, 
                    respiratory_rate, measurement_time, notes
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                record["appointment_id"],
                record["nurse_id"],
                record["temperature"],
                record["blood_pressure"],
                record["pulse"],
                record["respiratory_rate"],
                record["measurement_time"],
                record["notes"]
            ))
        
        # Commit the transaction
        conn.commit()
        print("Data successfully inserted into the vital_signs table!")
    
    except Exception as e:
        print(f"Failed to insert data: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Run the function
if __name__ == "__main__":
    data = load_data("./vital_signs.json")  # Ensure vital
    insert_vital_signs_data(data, db_config)