import psycopg2
from psycopg2 import sql

class DB:
    # 靜態變量用於存儲連接對象
    conn = None

    @staticmethod
    def init_connection(db_config):
        """
        初始化數據庫連接
        :param db_config: 包含數據庫配置信息的字典
        """
        if DB.conn is None:  # 確保只創建一次連接
            DB.conn = psycopg2.connect(
                dbname=db_config["dbname"],
                user=db_config["user"],
                password=db_config["password"],
                host=db_config["host"],
                port=db_config["port"]
            )

    @staticmethod
    def connect():
        """
        獲取數據庫游標
        :return: 游標對象
        """
        if DB.conn is None:
            raise Exception("Database connection not initialized. Call init_connection first.")
        return DB.conn.cursor()

    @staticmethod
    def execute(cursor, sql):
        """
        執行 SQL 語句
        :param cursor: 游標對象
        :param sql: 要執行的 SQL 語句
        :return: 游標對象
        """
        cursor.execute(sql)
        return cursor

    @staticmethod
    def execute_input(cursor, sql, inputs):
        """
        執行帶參數的 SQL 語句
        :param cursor: 游標對象
        :param sql: 要執行的 SQL 語句
        :param inputs: SQL 語句的參數
        """
        cursor.execute(sql, inputs)

    @staticmethod
    def fetchall(cursor):
        """
        獲取所有查詢結果
        :param cursor: 游標對象
        :return: 查詢結果列表
        """
        return cursor.fetchall()

    @staticmethod
    def fetchone(cursor):
        """
        獲取單行查詢結果
        :param cursor: 游標對象
        :return: 單行查詢結果
        """
        return cursor.fetchone()

    @staticmethod
    def commit():
        """
        提交當前事務
        """
        if DB.conn is not None:
            DB.conn.commit()

    @staticmethod
    def close_connection():
        """
        關閉數據庫連接
        """
        if DB.conn is not None:
            DB.conn.close()
            DB.conn = None
