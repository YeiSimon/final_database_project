from db.DB import DB

class Appointment:
    @staticmethod
    def create_appointment(input):
        """
        創建新預約
        :param input: 預約所需的參數，按順序對應 SQL 中的佔位符
        """
        sql = """
        INSERT INTO appointments (patient_id, doctor_id, nurse_id, appointment_time, status, 
                                   diagnosis, appointment_type, visit_type, session, is_emergency, 
                                   follow_up_to)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, input)
        DB.commit()

    @staticmethod
    def get_appointment(appointment_id):
        """
        根據預約 ID 獲取預約詳細信息
        :param appointment_id: 預約的主鍵 ID
        :return: 預約的詳細信息（字典形式）或 None
        """
        sql = "SELECT * FROM appointments WHERE appointment_id = %s"
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, [appointment_id])
            return DB.fetchone(cursor)

    @staticmethod
    def update_appointment(appointment_id, updates):
        """
        更新預約信息
        :param appointment_id: 要更新的預約 ID
        :param updates: 包含更新的參數，按順序對應 SQL 中的佔位符
        """
        sql = """
        UPDATE appointments
        SET patient_id = %s, doctor_id = %s, nurse_id = %s, appointment_time = %s, status = %s,
            diagnosis = %s, appointment_type = %s, visit_type = %s, session = %s, is_emergency = %s,
            follow_up_to = %s, updated_at = CURRENT_TIMESTAMP
        WHERE appointment_id = %s
        """
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, updates + [appointment_id])
        DB.commit()

    @staticmethod
    def delete_appointment(appointment_id):
        """
        刪除預約
        :param appointment_id: 要刪除的預約 ID
        """
        sql = "DELETE FROM appointments WHERE appointment_id = %s"
        with DB.connect() as cursor:
            DB.execute_input(cursor, sql, [appointment_id])
        DB.commit()
