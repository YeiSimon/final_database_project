import DB
class Medication:
    def create_medication(input):
        sql = """
        INSERT INTO medications (appointment_id, medication_name, dosage, frequency, duration, 
                                 additional_instructions)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        DB.execute_input(DB.connect(), sql, input)
        DB.commit()

    def get_medication(medication_id):
        sql = "SELECT * FROM medications WHERE medication_id = %s"
        return DB.fetchone(DB.execute_input(DB.connect(), sql, [medication_id]))

    def update_medication(medication_id, updates):
        sql = """
        UPDATE medications
        SET appointment_id = %s, medication_name = %s, dosage = %s, frequency = %s, duration = %s, 
            additional_instructions = %s, updated_at = CURRENT_TIMESTAMP
        WHERE medication_id = %s
        """
        DB.execute_input(DB.connect(), sql, updates + [medication_id])
        DB.commit()

    def delete_medication(medication_id):
        sql = "DELETE FROM medications WHERE medication_id = %s"
        DB.execute_input(DB.connect(), sql, [medication_id])
        DB.commit()
