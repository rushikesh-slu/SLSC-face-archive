from flask import Flask, Blueprint, send_from_directory, request
from flask_cors import CORS
from api.user import user
import os

app = Flask(__name__, static_folder='./../frontend/SLSCFaceTagging/dist/slscface-tagging')
CORS(app)

app.register_blueprint(user,url_prefix='/api')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
