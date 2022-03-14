import sqlite3


class Database:
    """
    Data basa nomini kiriting
    Avtomatik nomlanishi main.db
    """

    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=None, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_gr(self):
        sql = """
        CREATE TABLE Groups (
            id     INTEGER       PRIMARY KEY AUTOINCREMENT,
            group_name STRING (32) NOT NULL UNIQUE
            );
        """

        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_group(self, group_name):
        """
        Obunachi qo'shish uchun funksiya.
        Ushbu funksiyadan, obunachini bazaga qo'shishda foydalaning
        """
        sql = """
        INSERT INTO Groups (group_name) VALUES (?);
        """
        self.execute(sql, parameters=(group_name,), commit=True)

    def select_all_gr(self):
        sql = """
        SELECT group_name FROM Groups
        """
        return self.execute(sql, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Groups;", fetchone=True)

    def delete_product(self, desc):
        return self.execute("DELETE FROM products WHERE description=?", (desc,), commit=True)


def logger(statement):
    pass
    # print(f"Executing: -- {statement}")