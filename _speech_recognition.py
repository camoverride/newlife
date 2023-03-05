import subprocess
import wave

# https://pypi.org/project/SpeechRecognition/
# https://libraries.io/pypi/SpeechRecognition
import speech_recognition as sr



class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # self.recognizer.pause_threshold = 0.8
        self.recognizer.dynamic_energy_threshold = False # stop mic from recording ambient noise


    def get_audio(self, source):
        """
        This method listens to incoming audio and determines which "chunk" should
        be considered a valid speech signal for downstream processing.

        IMPORTANT: this method uses the speech_recognition library, and can probably be run
        offline. It simply records the intensity of the audio input and waits for it to
        tail off. Not sure how "modern" this approach is. See: https://github.com/Uberi/speech_recognition/blob/010382b80267f0f7794169fccc8e875ee7da7c19/speech_recognition/__init__.py#L632
        This makes use of zero crossing rate: https://en.wikipedia.org/wiki/Zero-crossing_rate
        Find a better VAD: https://thegradient.pub/one-voice-detector-to-rule-them-all/

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
                return self.recognizer.listen(source, timeout=10, config=dict(language_code="en-US"))
            except:
                return False
        except sr.UnknownValueError: # TODO: self.
            return False


    def speech_to_text(self, audio):
        """
        ASR - Automagic Speech Recognition
        Tracks some incoming audio and converts it to a string.

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
