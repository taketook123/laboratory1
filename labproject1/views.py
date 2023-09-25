from labproject1 import app
from datetime import datetime
from flask import jsonify

@app.route('/healthcheck')
def healthcheck_page():
    cur_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    response = {
        "status": "succes",
        "message": "Code of response: 200",
        "current_date": cur_date    
    }
    return jsonify(response)
