import configparser
import json
import sqlite3
from flask import Flask, jsonify
import os

app = Flask(__name__)

db_file = 'config_data.db'
config_file = 'sample_config.ini'

# 1. Read configuration file and parse key-value pairs
def parse_config(file_path):
    config = configparser.ConfigParser()
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")

    try:
        config.read(file_path)
        config_dict = {section: dict(config.items(section)) for section in config.sections()}
        return config_dict
    except Exception as e:
        raise RuntimeError(f"Error reading config file: {e}")

# 2. Save parsed config to SQLite DB as JSON
def save_to_database(data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS configurations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data TEXT NOT NULL
                      )''')
    cursor.execute("INSERT INTO configurations (data) VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()

# 3. API to fetch data
@app.route('/config', methods=['GET'])
def get_config():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM configurations ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify(json.loads(row[0]))
    else:
        return jsonify({"error": "No configuration data found."}), 404

if __name__ == '__main__':
    try:
        config_data = parse_config(config_file)
        print("Configuration File Parser Results:")
        for section, items in config_data.items():
            print(f"\n{section}:")
            for key, value in items.items():
                print(f"- {key}: {value}")

        save_to_database(config_data)
    except Exception as e:
        print(f"Error: {e}")

    app.run(debug=True)
