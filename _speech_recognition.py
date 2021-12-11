import subprocess
import wave

import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # self.recognizer.pause_threshold = 0.8
        self.recognizer.dynamic_energy_threshold = False # stop mic from recording ambient noise


    def get_audio(self, source):
        """
        This method listens to incoming audio and determines which "chunk" should
        be considered a valid speech signal for downstream processing

        Parameters
        ----------
        source : TODO: what format is this?
            An incoming audio stream that (hopefully) contains a speech signal.

        Returns
        -------
        TODO: what format is this?
        """
        try:
            try:
                return self.recognizer.listen(source, timeout=10)
            except:
                return False
        except sr.UnknownValueError: # TODO: self.
            return False


    def speech_to_text(self, audio):
        """
        ASR - Automagic Speech Recognition
        Tracks some incoming audio and converts it to a string.
        TODO: find a lightweight library that will run on Pi

        Parameters
        ----------
        audio : TODO: what format is this?
            An audio file that corresponds to a speech signal.
        
        Returns
        -------
        str
            The string that corresponds to the written representation of the audio.
        """
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return False
