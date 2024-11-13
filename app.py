from flask import Flask, jsonify, Response, send_file

app = Flask(__name__)

# Respond with JSON
@app.route('/data.json')
def json_data():
    return jsonify({"name": "Sample Data", "value": 12345})

# Respond with XML
@app.route('/data.xml')
def xml_data():
    xml = '<data><name>Sample Data</name><value>12345</value></data>'
    return Response(xml, mimetype='application/xml')

# Respond with CSV
@app.route('/data.csv')
def csv_data():
    csv = 'name,value\nSample Data,12345\n'
    return Response(csv, mimetype='text/csv')

# Serve HTML
@app.route('/')
def index():
    return "Just Normal"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
