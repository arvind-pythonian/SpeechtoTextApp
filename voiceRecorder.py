from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from main.config import DevelopmentConfig
from main.mongo_config import setup_mongo_connection
from services.speechtotext import SpeechToText, AUDIO_FILE

flask_bcrypt = Bcrypt()
app = Flask(__name__)


@app.route('/')
def init_recorder():
    return render_template('index.html')


@app.route('/uploads', methods=['POST'])
def save_audio1():
    with open(AUDIO_FILE, 'wb') as f:
        # writing the raw audio data to audio file using context
        f.write(request.data)
    transcription = SpeechToText.convert()  # Getting the converted transription
    return transcription


if __name__ == '__main__':
    setup_mongo_connection()  # establishing connection to mongoDB
    flask_bcrypt.init_app(app)
    app.run(debug=True, port=5000)
