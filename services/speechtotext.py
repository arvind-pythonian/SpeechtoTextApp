import speech_recognition as sr
from os import path
from main.config import DevelopmentConfig
from services.transcription_service import TranscriptionService

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), DevelopmentConfig.AUDIO_FILE_PATH)


class SpeechToText:
    @staticmethod
    def convert():
        try:
            # use the audio file as the audio source
            r = sr.Recognizer()
            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                transcription = r.recognize_google(audio)  # recognised transcription
                if TranscriptionService.save_transcriptions(transcription):
                    return "Speech Recognition thinks you said " + transcription
                else:
                    return "There's an error Processing the transcription."
            except sr.UnknownValueError:
                return "Speech Recognition could not understand audio"
            except sr.RequestError as e:
                return "Could not request results from Speech Recognition service; {0}".format(e)
        except sr.RequestError as e:
            return "Could not request results from Speech Recognition service; {0}".format(e)
        except:
            return "Error Initializing Speech Recognition Service."
