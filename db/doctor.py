from db.DB import DB

class Doctor:
    @staticmethod
    def create_doctor(input):
        sql = """
        INSERT INTO doctors (name, specialization, phone, email, department, license_number)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, input)
        DB.commit()

    @staticmethod
    def get_doctor(doctor_id):
        sql = "SELECT * FROM doctors WHERE doctor_id = %s"
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, [doctor_id])
            return DB.fetchone(cursor)

    @staticmethod
    def update_doctor(doctor_id, updates):
        sql = """
        UPDATE doctors
        SET name = %s, specialization = %s, phone = %s, email = %s, department = %s, license_number = %s, 
        updated_at = CURRENT_TIMESTAMP
        WHERE doctor_id = %s
        """
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, updates + [doctor_id])
        DB.commit()

    @staticmethod
    def delete_doctor(doctor_id):
        sql = "DELETE FROM doctors WHERE doctor_id = %s"
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, [doctor_id])
        DB.commit()

    