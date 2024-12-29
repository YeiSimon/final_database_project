import json
import psycopg2
from psycopg2.extras import execute_values

# Database configuration
db_config = {
    "dbname": "clinic_db",
    "user": "clinic_user",
    "password": "clinic_password",
    "host": "localhost",
    "port": "5432"
}

def insert_appointments(data, db_config):
    """
    Insert appointment data into the appointments table.

    Args:
        data (list of dict): List of appointment records.
        db_config (dict): Database connection configuration.

    Returns:
        None
    """
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # SQL query for batch insertion
        query = """
            INSERT INTO appointments (
                appointment_id, patient_id, doctor_id, nurse_id, appointment_time, status,
                completed_time, diagnosis, appointment_type, visit_type, session, 
                is_emergency, follow_up_to
            )
            VALUES %s
            ON CONFLICT (appointment_id) DO NOTHING
        """

        # Prepare data for execute_values
        values = [
            (
                record["appointment_id"],
                record["patient_id"],
                record["doctor_id"],
                record["nurse_id"],
                record["appointment_time"],
                record["status"],
                record["completed_time"],
                record["diagnosis"],
                record["appointment_type"],
                record["visit_type"],
                record["session"],
                record["is_emergency"],
                record["follow_up_to"]
            )
            for record in data
        ]

        # Use execute_values for batch insertion
        execute_values(cursor, query, values)

        # Commit the transaction
        conn.commit()
        print(f"Successfully inserted {len(values)} records into the appointments table!")

    except psycopg2.OperationalError as conn_error:
        print(f"Database connection failed: {conn_error}")

    except psycopg2.Error as sql_error:
        print(f"SQL execution failed: {sql_error}")
        if conn:
            conn.rollback()  # Rollback in case of an SQL error

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    try:
        # Load data from a JSON file or directly from a string
        json_file_path = "./appointments.json"
        
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Validate data
        if not data:
            print("No data found in the file.")
        else:
            insert_appointments(data, db_config)
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except json.JSONDecodeError as json_error:
        print(f"Error parsing JSON data: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
