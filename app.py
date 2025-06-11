from flask import Flask
from flask_cors import CORS

from routes.iNGS.subtitles import *

app = Flask(__name__)

allowed_origins = ["https://localhost:4200"]
CORS(app, resources={r"app/*": {"origins": allowed_origins}})

@app.route('/api/getNotes', methods = ['GET'])
def fetch_notes():
    return fetchNotesFromURL()

if (__name__ == "__main__"):
    app.run(debug=True)