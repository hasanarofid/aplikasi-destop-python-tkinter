import sqlite3

def create_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')

    default_user = ('admin', 'admin123')
    cursor.execute('''INSERT OR IGNORE INTO user (username, password)
                      VALUES (?, ?)''', default_user)

    conn.commit()
    conn.close()

def verify_login(username, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM user WHERE username=? AND password=?''', (username, password))
    user_data = cursor.fetchone()

    conn.close()
    return user_data is not None
