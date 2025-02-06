from flask import Flask, jsonify
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def get_info():
	response = {
		"email": "akpanabraham1000@gmail.com",
		"current_datetime": datetime.utcnow().isoformat() + "Z",
		"github_url": "https://github.com/Ab-Ezekiel/HNG12_stage0_public_api.git"
	}
	return jsonify(response), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
