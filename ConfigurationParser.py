import configparser
import json
from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/configparser.ini")  # Replace with Atlas URI if needed

db = mongo_client['assignment']
collection = db['config']

# Configuration file path
base_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(base_dir, 'sample_config.ini')

# 1. Read configuration file and parse key-value pairs
def parse_config(file_path):
    config = configparser.ConfigParser()
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")

    try:
        config.read(file_path)
        config_dict = {section: dict(config.items(section)) for section in config.sections()}
        if not config_dict:
            raise ValueError("No valid config sections found.")
        return config_dict
    except Exception as e:
        raise RuntimeError(f"Error reading config file: {e}")

# 2. Save parsed config to MongoDB as JSON
def save_to_database(data):
    result = collection.insert_one({"data": data})
    print(f"Data inserted with ID: {result.inserted_id}")

# 3. API to fetch data
@app.route('/config', methods=['GET'])
def get_config():
    latest = collection.find_one(sort=[('_id', -1)])
    if latest:
        return jsonify(latest["data"])
    else:
        return jsonify({"error": "No configuration data found."}), 404


# Optional: Load on app startup
@app.before_request
def init_app():
    if not hasattr(app, 'config_initialized'):
        try:
            config_data = parse_config(config_file)
            print("Parsed config:")
            for section, items in config_data.items():
                print(f"\n[{section}]")
                for k, v in items.items():
                    print(f"{k} = {v}")
            save_to_database(config_data)
            app.config_initialized = True  # Prevent re-initializing
        except Exception as e:
            print(f"Initialization error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
