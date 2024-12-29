import DB

class Patient:
    def create_patient(input):
        sql = """
        INSERT INTO patients (name, phone, email, address, birth_date, medical_history, has_ic_card, ic_card_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        DB.execute_input(DB.connect(), sql, input)
        DB.commit()

    def get_patient(patient_id):
        sql = "SELECT * FROM patients WHERE patient_id = %s"
        return DB.fetchone(DB.execute_input(DB.connect(), sql, [patient_id]))

    def update_patient(patient_id, updates):
        sql = """
        UPDATE patients
        SET name = %s, phone = %s, email = %s, address = %s, birth_date = %s, medical_history = %s, 
        has_ic_card = %s, ic_card_number = %s, updated_at = CURRENT_TIMESTAMP
        WHERE patient_id = %s
        """
        DB.execute_input(DB.connect(), sql, updates + [patient_id])
        DB.commit()

    def delete_patient(patient_id):
        sql = "DELETE FROM patients WHERE patient_id = %s"
        DB.execute_input(DB.connect(), sql, [patient_id])
        DB.commit()