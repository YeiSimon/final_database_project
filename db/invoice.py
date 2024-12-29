import DB
class Invoice:
    def create_invoice(input):
        sql = """
        INSERT INTO invoices (appointment_id, registration_fee, medical_fee, total_amount, 
                              is_paid, payment_time, payment_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        DB.execute_input(DB.connect(), sql, input)
        DB.commit()

    def get_invoice(invoice_id):
        sql = "SELECT * FROM invoices WHERE invoice_id = %s"
        return DB.fetchone(DB.execute_input(DB.connect(), sql, [invoice_id]))

    def update_invoice(invoice_id, updates):
        sql = """
        UPDATE invoices
        SET appointment_id = %s, registration_fee = %s, medical_fee = %s, total_amount = %s, 
            is_paid = %s, payment_time = %s, payment_type = %s, updated_at = CURRENT_TIMESTAMP
        WHERE invoice_id = %s
        """
        DB.execute_input(DB.connect(), sql, updates + [invoice_id])
        DB.commit()

    def delete_invoice(invoice_id):
        sql = "DELETE FROM invoices WHERE invoice_id = %s"
        DB.execute_input(DB.connect(), sql, [invoice_id])
        DB.commit()
