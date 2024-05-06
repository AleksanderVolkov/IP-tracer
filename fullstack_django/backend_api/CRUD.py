import sqlite3

def read_data_base():
    connection = sqlite3.connect("IP.bd")
    cursor = connection.cursor()
    cursor.execute("SELECT IPorLink FROM IP")
    frames = cursor.fetchall()
    connection.close()
    #answer = []
    for frame in frames:
        #answer.append(frame)
        print(f"IPorLink: {frame}")
    #return answer

def create_data_base():
    connection = sqlite3.connect("IP.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS IP (
        id TEXT PRIMARY KEY,
        IPorLink TEXT
        )
    ''')
    connection.commit()
    connection.close()

def append_data(ip_dns):
    connection = sqlite3.connect("IP.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO IP (IPorLink) VALUES (?)', (ip_dns,))
    connection.commit()
    connection.close()

def delete_line():
    connection = sqlite3.connect("IP.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from IP where id = (SELECT MAX(id) FROM IP)")
    connection.commit()

if __name__ == "__main__":
    read_data_base()