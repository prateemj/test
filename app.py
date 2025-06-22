from flask import Flask
from flask_cors import CORS

from routes.iNGS.subtitles import *

app = Flask(__name__)

allowed_origins = ["http://localhost:4200", "https://ings-frontend.onrender.com"]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/api/extractSubtitlesFromURL', methods = ['POST'])
def fetch_notes_from_url():
    return fetchNotesFromURL()

@app.route('/api/extractSubtitlesFromFile', methods = ['POST'])
def fetch_notes_from_file():
    return fetchNotesFromFile()

if (__name__ == "__main__"):
    app.run(debug=True)