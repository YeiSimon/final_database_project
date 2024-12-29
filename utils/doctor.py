import psycopg2 
from utils import load_data

def insert_data_to_postgres(datas, db_config):
    try:
        # 建立資料庫連線
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        cursor = conn.cursor()

        # 插入資料
        for data in datas:
            cursor.execute("""
                INSERT INTO doctors (name, specialization, phone, department, license_number)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data.get("name", "").strip(),
                data.get("specialization", "").strip(),
                data.get("phone", "").strip(),
                data.get("department", "").strip(),
                data.get("license_number", "").strip(),
            ))
        conn.commit()
        print("資料已成功插入 PostgreSQL 資料庫！")
    except Exception as e:
        print(f"資料插入失敗：{e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    input_file = "doctor.json"  # 篩選後的 JSON 檔案路徑

    # PostgreSQL 資料庫設定
    db_config = {
        "dbname": "clinic_db",
        "user": "clinic_user",
        "password": "clinic_password",
        "host": "localhost",  # e.g., "localhost"
        "port": "5432"  # PostgreSQL 預設端口
    }

    datas = load_data(input_file)[:10]
    insert_data_to_postgres(datas, db_config)