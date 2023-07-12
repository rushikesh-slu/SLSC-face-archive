from flask import Flask, Blueprint, send_from_directory, render_template,request,make_response
from flask_cors import CORS

from api.user import user



app = Flask(__name__, static_folder='')

app.register_blueprint(user,url_prefix='/api')


@app.route('/assets/<path:filename>')
def custom_static_for_assets(filename):
    return send_from_directory('assets', filename)


@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('', filename)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)