# TODO: print debug somewhere - modify print statements

#! /usr/bin/env python

# For checkpointing model runtime on low-power devices (raspberry pi zero)
from datetime import datetime
import time

import speech_recognition as sr
from gtts_lang_codes import check_for_translation_change


from _speech_recognition import SpeechRecognizer
from _generate_response import ResponseGenerator
from _text_to_speech import TextToSpeech


class Persona:
    """
    This class defines an individual AI chatbot entity. The chatbot will be referred
    to as "bot" and the entity the bot converses with as "human." There's only one public
    method, `converse`, and it calls four private methods that are taken from classes
    defined elsewhere:

    1) self._speech_to_text.get_audio - determines what segment of speech should be processed.
    2) self._speech_to_text.speech_to_text - performs ASR (Automatic Speech Recognition) to get the text.
    3) self._generate_response.generate_response - determines an appropriate reply.
    4) self._text_to_speech.text_to_speech - performs TTS (Text to Speech) so the bot can speak. TODO: custom voices.
    """

    def __init__(self, name, mode, language, rules_only=True):
        """
        Declare the properties of the chatbot that is being created.

        Parameters
        ----------
        name : str
            The name of the individual chatbot personality.
        voice : int
            The integer corresponding to the voice that will speak.
        volume_level : int
            How loud the voice should be
        """
        # ASR Properties
        self._speech_to_text = SpeechRecognizer()

        # Response Properties
        self._generate_response = ResponseGenerator(name=name, rules_only=rules_only)

        # TTS Properties
        self._text_to_speech = TextToSpeech()

        # Conversation properties
        self.mode = mode
        self.language = language


    def converse(self):
        """
        Starts the loop that listens for user audio.
        """
        print("Conversation Started!")

        if self.mode == "translate":
            response_ = self._generate_response.translate("hello, let's talk!", language=self.language)
            self._text_to_speech.text_to_speech(response_, language=self.language)
        else:
            self._text_to_speech.text_to_speech("hello")


        while True:
            # Begin the audio stream
            with sr.Microphone() as source:
                print("--------------------")

                print("1) Listen ..........")
                audio = self._speech_to_text.get_audio(source)

                # ASR
                print("2) ASR .............")
                time.sleep(0.1) # add latency so the script can be more elegantly killed
                start = datetime.now()
                transcription = None
                if audio:
                    transcription = self._speech_to_text.speech_to_text(audio)

                if transcription:
                    # ASR INFO
                    end = datetime.now()
                    print(f"... {transcription}")
                    print(f"total seconds: {(end - start).total_seconds()}")


                    # Change mode
                    if transcription == "mode translate":
                        self.mode = "translate"
                    elif transcription == "mode Echo":
                        self.mode = "echo"
                    elif transcription == "mode chat":
                        self.mode = "chat"


                    # Change translation language
                    # If the human says "translate X," the language will change to X.
                    # e.g. "translate Indonesian"
                    lc = check_for_translation_change(transcription)
                    if lc:
                        self.language = lc


                    print("3) Knowledge .......")
                    start = datetime.now()
                    if not transcription and self.mode == "translate":
                        response = " "
                    elif not transcription:
                        response = self._generate_response.default_say_more()

                    elif self.mode == "echo":
                        response = transcription
                    elif self.mode == "translate":
                        response = self._generate_response.translate(transcription, language=self.language)
                    else:
                        response = self._generate_response.generate_response(transcription)
                    # Knowledge INFO
                    end = datetime.now()
                    print(f"... {response}")
                    print(f"total seconds: {(end - start).total_seconds()}")


                    # TTS
                    print("4) TTS .............")
                    start = datetime.now()
                    self._text_to_speech.text_to_speech(response, language=self.language)
                    # TTS INFO
                    end = datetime.now()
                    print(f"total seconds: {(end - start).total_seconds()}")

                else:
                    pass


if __name__ == "__main__":

    # Create an individual AI agent
    starting_mode = "translate" # starting modes = "chat", "echo", "translate"
    starting_language = "es" # for other options see `gtts_lang_codes.py`
    persona_Cam2 = Persona(name="Cam2.0", mode=starting_mode, language=starting_language)

    # Start the chat session
    persona_Cam2.converse()
