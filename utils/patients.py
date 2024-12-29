from utils import load_data
import psycopg2

db_config = {
        "dbname": "clinic_db",
        "user": "clinic_user",
        "password": "clinic_password",
        "host": "localhost",  # e.g., "localhost"
        "port": "5432"  # PostgreSQL 預設端口
    }

# Function to insert data into PostgreSQL
def insert_patients_data(data, db_config):
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

        # Insert each record into the patients table
        for record in data:
            cursor.execute("""
                INSERT INTO patients (name, phone, email, address, birth_date, medical_history, has_ic_card, ic_card_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                record["name"],
                record["phone"],
                record["email"],
                record["address"],
                record["birth_date"],
                record["medical_history"],
                record["has_ic_card"],
                record["ic_card_number"]
            ))
        
        # Commit the transaction
        conn.commit()
        print("Data successfully inserted into the patients table!")
    
    except Exception as e:
        print(f"Failed to insert data: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Run the function
if __name__ == "__main__":
    data = load_data("./patients.json")
    insert_patients_data(data, db_config)
