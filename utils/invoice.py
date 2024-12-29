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

def insert_invoices(data, db_config):
    """
    Inserts invoice data into the invoices table.

    Args:
        data (list of dict): List of invoice records.
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
            INSERT INTO invoices (
                invoice_id, appointment_id, registration_fee, medical_fee, 
                total_amount, is_paid, payment_time, payment_type, created_at, updated_at
            )
            VALUES %s
            ON CONFLICT (invoice_id) DO NOTHING
        """

        # Prepare data for execute_values
        values = [
            (
                record["invoice_id"],
                record["appointment_id"],
                record["registration_fee"],
                record["medical_fee"],
                record["total_amount"],
                record["is_paid"],
                record["payment_time"],
                record["payment_type"],
                record["created_at"],
                record["updated_at"]
            )
            for record in data
        ]

        # Use execute_values for batch insertion
        execute_values(cursor, query, values)

        # Commit the transaction
        conn.commit()
        print(f"Successfully inserted {len(values)} records into the invoices table!")

    except psycopg2.OperationalError as conn_error:
        print(f"Database connection failed: {conn_error}")

    except psycopg2.Error as sql_error:
        print(f"SQL execution failed: {sql_error}")
        conn.rollback()  # Rollback in case of an SQL error

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    try:
        # Load invoice data from JSON file or directly from a variable
        json_file_path = "./invoice.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Validate data
        if not data:
            print("No data found in the file.")
        else:
            insert_invoices(data, db_config)
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except json.JSONDecodeError as json_error:
        print(f"Error parsing JSON data: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
