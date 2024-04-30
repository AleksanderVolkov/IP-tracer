import sqlite3

def read_data_base():
    connection = sqlite3.connect("our_data_base.bd")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM our_data_base")
    frames = cursor.fetchall()
    connection.close()
    for frame in frames:
        print(f"id: {frame[0]}, text: {frame[1]}")

def create_data_base():
    connection = sqlite3.connect("our_data_base.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS our_data_base (
        id INTEGER PRIMARY KEY,
        text TEXT
        )
    ''')
    connection.commit()
    connection.close()

def append_data(ip):
    connection = sqlite3.connect("our_data_base.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO our_data_base (text) VALUES (?)', (ip))
    connection.commit()
    connection.close()

def delete_line():
    connection = sqlite3.connect("our_data_base.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from our_data_base where id = (SELECT MAX(id) FROM our_data_base)")
    connection.commit()

if __name__ == "__main__":
    read_data_base()