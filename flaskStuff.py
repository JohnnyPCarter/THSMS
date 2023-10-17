from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
database = "MediaCenter.db"


@app.route('/get_data', methods=['GET'])
def get_data():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM files ORDER BY CreatedDate DESC LIMIT 10;')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/add_data', methods=['POST'])
def add_data():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute('INSERT INTO files (FileName, Region, CreatedDate) VALUES (?, ?, ?);', (data['FileName'], data['Region'], data['CreatedDate']))
    conn.commit()
    conn.close()
    return 'Data added successfully'

if __name__ == '__main__':
    app.run(port=5000)
