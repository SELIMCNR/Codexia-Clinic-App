import hashlib
import sqlite3
import re

class UserModel:
    def __init__(self, db_path="clinic.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            security_question TEXT,
            security_answer TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()


    def is_valid_password(self, password):
        if len(password) < 6:
            return False
        pattern = r"^(?=.*[a-zA-Z])(?=.*\d).{6,}$"
        return re.match(pattern, password) is not None
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def hash_answer(self, answer):
        return hashlib.sha256(answer.lower().strip().encode()).hexdigest()

    def verify_user(self, username, password):
        hashed = self.hash_password(password)
        query = "SELECT role FROM users WHERE username=? AND password=?"
        cursor = self.conn.execute(query, (username, hashed))
        result = cursor.fetchone()
        return result[0] if result else None

    def add_user(self, username, password, role, question=None, answer=None):
        hashed_pw = self.hash_password(password)
        hashed_ans = self.hash_answer(answer) if answer else None
        query = """
        INSERT INTO users (username, password, role, security_question, security_answer)
        VALUES (?, ?, ?, ?, ?)
        """
        try:
            self.conn.execute(query, (username, hashed_pw, role, question, hashed_ans))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_security_question(self, username):
        query = "SELECT security_question FROM users WHERE username=?"
        cursor = self.conn.execute(query, (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def verify_security_answer(self, username, answer):
        hashed_ans = self.hash_answer(answer)
        query = "SELECT id FROM users WHERE username=? AND security_answer=?"
        cursor = self.conn.execute(query, (username, hashed_ans))
        return cursor.fetchone() is not None

    def update_password(self, username, new_password):
        hashed_pw = self.hash_password(new_password)
        query = "UPDATE users SET password=? WHERE username=?"
        self.conn.execute(query, (hashed_pw, username))
        self.conn.commit()

    def get_all_users(self):
        query = "SELECT id, username, role FROM users ORDER BY username"
        return self.conn.execute(query).fetchall()

    def update_role(self, user_id, new_role):
        query = "UPDATE users SET role=? WHERE id=?"
        self.conn.execute(query, (new_role, user_id))
        self.conn.commit()

    def reset_password(self, user_id, new_password):
        query = "UPDATE users SET password=? WHERE id=?"
        self.conn.execute(query, (new_password, user_id))
        self.conn.commit()
        