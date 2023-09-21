from labproject1 import app

@app.route('/healthcheck')
def healthcheck_page():
    return "<p>Healthcheck endpoint</p>"
