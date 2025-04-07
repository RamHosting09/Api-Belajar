from flask import Flask, jsonify
app = Flask(__name__)
data_api = {
    "nama": "RamHosting09",
    "alamat": "Indonesia",
    "kontak": "1234567890"
}
@app.route('/api/info', methods=['GET'])
def info():
    return jsonify(data_api)
if __name__ == '__main__':
    app.run(debug=True)
