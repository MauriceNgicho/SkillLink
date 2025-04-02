from flask import Flask, jsonify, make_response
from flask_cors import CORS
from api.v1.views import api_views
from os import environ
from models import storage

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Register Blueprints for API endpoints
app.register_blueprint(api_views)

cors = CORS(app, resources={r"/api/v1*":{"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """Close db session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handle 404 error"""
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    host = environ.get('SKILLLINK_API_HOST', '0.0.0.0')
    port = environ.get('SKILLLINK_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)