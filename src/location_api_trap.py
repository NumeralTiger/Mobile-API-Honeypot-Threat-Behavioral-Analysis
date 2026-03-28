import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging for "Research Data"
logging.basicConfig(filename='threat_intelligence.log', level=logging.INFO)

@app.route('/api/v1/user/location', methods=['GET', 'POST'])
def fake_location_api():
    attacker_data = {
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent'),
        "payload": request.get_data(as_text=True),
        "intent": "Unauthorized Location Access Attempt"
    }
    # Log the behavior for "Statistical Analysis" (CRL loves this term)
    logging.info(f"RESEARCH_DATA: {attacker_data}")
    
    # Return a realistic "Privacy Paradox" response
    return jsonify({"status": "error", "message": "Permission Denied: Location Sharing Disabled"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
