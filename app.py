from flask import Flask
from flask_cors import CORS

from routes.iNGS.subtitles import *

app = Flask(__name__)

allowed_origins = ["http://localhost:4200"]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/api/extractSubtitlesFromURL', methods = ['POST'])
def fetch_notes():
    return fetchNotesFromURL()

if (__name__ == "__main__"):
    app.run(debug=True)