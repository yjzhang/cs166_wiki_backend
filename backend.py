import sqlite3
import time

import flask
from flask import Flask

app = Flask(__name__)

db_dir = '/home/yjzhang/privacy/database.db'

@app.route('/')
def index():
    return 'testing'

@app.route('/save_browser_hash')
def save_browser_data(hash, ip, lat = "", lon = ""):
    conn = sqlite3.connect(db_dir)
    cursor = conn.cursor()
    # let's completely ignore hash collisions
    cursor.execute('SELECT ip, datetime FROM ip_hashes WHERE hash=?', (hash,))
    results = cursor.fetchall()
    results_str = ""
    if len(results) > 0:
        for result in results:
            old_ip = result[0]
            timestamp = result[1]
            results_str += old_ip + ' ' + timestamp + '\n'
    else:
        cursor.execute('INSERT INTO hashes values (?)', (hash,))
    current_time = time.gmtime()
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', current_time)
    cursor.execute('INSERT INTO ip_hashes values (?, ?, ?, ?, ?)', (ip, hash, time_str, lat, lon))
    conn.commit()
    conn.close()
    return results_str

if __name__ == '__main__':
    app.run()
