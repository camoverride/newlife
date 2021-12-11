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
        translation = self.translator.translate(response, dest=language).text
        return translation

    
    def default_say_more(self):
        """
        """
        return random.choice(self.defaults["default_say_more"])


    def generate_response(self, response):
        """
        KNOWLEDGE BASE - the brains.
        Given some speech from a human, determines the bot's response. Checks the
        generic knowledge base first, then the knowledge specific to the identity
        - if more than one response is encoded, one is chosen at random.
        TODO: if the response is incomprehensible, return a `default_say_more`
        response that asks the user to repeat.
        If neither of these are triggered, use a model to generate text.

        Parameters
        ----------
        response : str
            Something that a human said to the bot.
        
        Returns
        -------
        str
            A reasonable response for a bot to make.
        """
        for k in self.knowledge["generic"].keys():
            if re.match(k, response):
                return random.choice(self.knowledge["generic"][k])

        for k in self.knowledge[self.name].keys():
            if re.match(k, response):
                return random.choice(self.knowledge[self.name][k])

        # TODO: create function to see if response makes sense!
        response_incomprehensible = False

        if not self.rules_only and response_incomprehensible:
            # TODO: add GPT model backup
            pass

        return self.default_say_more()
