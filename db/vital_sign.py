import DB
class VitalSigns:
    def create_vital_sign(input):
        sql = """
        INSERT INTO vital_signs (appointment_id, nurse_id, temperature, blood_pressure, pulse, 
                                 respiratory_rate, measurement_time, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        DB.execute_input(DB.connect(), sql, input)
        DB.commit()

    def get_vital_sign(vital_signs_id):
        sql = "SELECT * FROM vital_signs WHERE vital_signs_id = %s"
        return DB.fetchone(DB.execute_input(DB.connect(), sql, [vital_signs_id]))

    def update_vital_sign(vital_signs_id, updates):
        sql = """
        UPDATE vital_signs
        SET appointment_id = %s, nurse_id = %s, temperature = %s, blood_pressure = %s, pulse = %s, 
            respiratory_rate = %s, measurement_time = %s, notes = %s, updated_at = CURRENT_TIMESTAMP
        WHERE vital_signs_id = %s
        """
        DB.execute_input(DB.connect(), sql, updates + [vital_signs_id])
        DB.commit()

    def delete_vital_sign(vital_signs_id):
        sql = "DELETE FROM vital_signs WHERE vital_signs_id = %s"
        DB.execute_input(DB.connect(), sql, [vital_signs_id])
        DB.commit()
