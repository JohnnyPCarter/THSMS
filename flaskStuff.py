from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
database = "MediaCenter.db"
CORS(app)


@app.route('/get_data', methods=['GET'])
def get_data():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('SELECT FileName FROM files ORDER BY CreatedDate DESC LIMIT 10;')
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

@app.route('/get_largest_id', methods=['GET'])
def get_largest_id():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM files;')
    largest_id = cursor.fetchone()[0]
    conn.close()
    return jsonify(largest_id)
'''
@app.route('/get_dataa_by_region/<region>', methods=['GET'])
def get_data(region):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('SELECT FileName FROM files WHERE Region = ? ORDER BY CreatedDate DESC LIMIT 10;', (region))
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
