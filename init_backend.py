import sqlite3

db_name = 'privacy.db'

if __name__ == '__main__':
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute('DROP TABLE hashes')
        cursor.execute('DROP TABLE ip_hashes')
    except:
        cursor.execute('CREATE TABLE hashes (hash text)')
        cursor.execute('CREATE TABLE ip_hashes (ip text, hash text, datetime text, lat text, lon text)')
    conn.commit()
    conn.close()
