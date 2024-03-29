from gtts import gTTS
import pygame



pygame.mixer.init()


class TextToSpeech:

    def __init__(self):
        pass


    def text_to_speech(self, response, language):
        """
        TTS - Text to Speech
        Converts some text to an audio file and plays it.

        Parameters
        ----------
        response : str
            Some text that you want to be spoken

        language : str
            The code for the language/dialect you want the response to be spoken in.
            See `gtts_lang_codes.py` for a mapping of language code to language name.

        Returns
        -------
        None
            Nothing is returned - instead, some audio is played.
        """
        tts = gTTS(response, lang=language)
        tts.save(".tts.mp3")

        pygame.mixer.music.load(".tts.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        
