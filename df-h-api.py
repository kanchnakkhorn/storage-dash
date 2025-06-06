from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/disk', methods=['GET'])
def get_disk_usage():
    try:
        result = subprocess.run(['df', '-h'], capture_output=True, text=True, check=True)
        return jsonify({"success": True, "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
