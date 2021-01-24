from datetime import datetime
from bson import ObjectId

from model.transcription import Transcriptions


class TranscriptionService:
    @staticmethod
    def save_transcriptions(transcription):
        try:
            _id = ObjectId()
            date = datetime.now()
            Transcriptions(_id, transcription, date).save()
            return True
        except:
            return False
