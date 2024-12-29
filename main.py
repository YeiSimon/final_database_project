from db.appointment import Appointment
from db.DB import DB

db_config = {
        "dbname": "clinic_db",
        "user": "clinic_user",
        "password": "clinic_password",
        "host": "localhost",  # e.g., "localhost"
        "port": "5432"  # PostgreSQL 預設端口
    }
    
    # 確保先初始化數據庫連接
DB.init_connection(db_config)
    
# 讀取單個醫生
appointment = Appointment.get_appointment(3) #查看id=3的預約結果
print(appointment)




