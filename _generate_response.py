import random
import re

from googletrans import Translator

from personas import knowledge as KNOWLEDGE
from personas import defaults as DEFAULTS


class ResponseGenerator:
    def __init__(self, name, rules_only):
        self.knowledge = KNOWLEDGE
        self.defaults = DEFAULTS
        self.name = name
        self.rules_only = rules_only

        # For translator
        self.translator = Translator()


    def translate(self, response, language):
        """
        Translates a incoming response into a given language.

        Parameters
        ----------
        response : str
            Something that a human said to the bot.
        language : str
            The language code that you want this translated to.
            See `gtts_lang_codes.py` for examples of this.

        Returns
        -------
        str
            A translation of the incoming text.
        """
        translation = self.translator.translate(response, dest=language).text
        return translation

    
    def default_say_more(self):
        """
        Selects from among several default phrases to prompt the user to say more.
        For example "can you say something else?"

        Parameters
        ----------
        None

        Returns
        -------
        str
            A string containing a prompt to say more.
        """
        return random.choice(self.defaults["default_say_more"])


    def generate_response(self, response):
        """
        Given some speech from a human, determines the bot's response. Checks the
        generic knowledge base first, then the knowledge specific to the identity
        - if more than one response is encoded, one is chosen at random.
        TODO: if the response is incomprehensible, return a `default_say_more`
        response that asks the user to repeat.
        TODO: If neither of these are triggered, use a model to generate text.

        Parameters
        ----------
        response : str
            Something that a human said to the bot.
        
        Returns
        -------
        str
            A reasonable response for a bot to make.
        """
        # Check the generic knowledge base that applies to all bots.
        for k in self.knowledge["generic"].keys():
            if re.match(k, response):
                return random.choice(self.knowledge["generic"][k])

        # Check the knowledge base specific to a persona
        for k in self.knowledge[self.name].keys():
            if re.match(k, response):
                return random.choice(self.knowledge[self.name][k])

        # TODO: create function to see if response makes sense!
        response_incomprehensible = False

        if not self.rules_only and response_incomprehensible:
            # TODO: add GPT model backup
            pass

        return self.default_say_more()
