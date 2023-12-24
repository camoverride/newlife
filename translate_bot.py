import logging
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from gtts_lang_codes import check_for_translation_change


# Global settings
logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.DEBUG)

recognizer = sr.Recognizer()
translator = Translator()
recognizer.dynamic_energy_threshold = False # stop mic from recording ambient noise
TRANSLATE_TO = "es"


while True:
    logging.debug("-------------------------------------------")
    with sr.Microphone() as source:
        text = None

        try:
            # Get Audio clip
            logging.debug("> Getting audio")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            # Speech-to-text
            logging.debug("> Speech to text")
            try:
                text = recognizer.recognize_google(audio, language="en-us")
            except sr.exceptions.UnknownValueError as e:
                logging.warning("ERROR recognizing speech. See below:")
                logging.warning(e)
                pass

        except sr.exceptions.WaitTimeoutError as e:
            logging.warning("ERROR getting audio. See below:")
            logging.warning(e)
            pass

        if text:
            logging.debug(f"Recognized text input: {text}")

            new_lang = check_for_translation_change(text)
            if new_lang:
                TRANSLATE_TO = new_lang
                logging.debug(f"Switched to {new_lang}")

            translation = translator.translate(text, dest=TRANSLATE_TO).text
            logging.debug(f"Translated text: {translation}")

            logging.debug("Translating text!")
            tts = gTTS(translation, lang=TRANSLATE_TO)
            tts.save(".tts.mp3")
            playsound(".tts.mp3")
