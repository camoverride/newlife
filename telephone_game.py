"""
This module coordinates interactions between several bots
playing the telephone game. It is called brain_server

bot_1 takes lang_1 as input and produces lang_2 as output
bot_2 takes lang_2 as input and produces lang_3 as output
...
the final bot should output lang_1

There is no need for bots to actually listen to each other.
It is sufficient for the telephone game's translation funcion
to be entirely performed by brain_server. The remote server
(this module) simply sends each bot the appropriate speech to
synthesize at the appropriate time. This requires communication
between the bots and brain_bot - because speech is synthesized
locally, the "end time" of a speech signal must be sent to the
coordinating server so it knows when to make the next bot start
speaking.

1) bot_1 performs ASR and sends the resulting text to brain_bot,
kicking off the chain
2) brain bot produces a "translation chain," by using Google
Translate to transform the text into lang_2, lang_3, etc
3) brain_bot sends the translated text to bot_2, which then sends
a message to brain_bot indicating that it is finished speaking
4) brain_bot then sends text to the next bot in the chain
5) repeat steps 3 and 4 until reaching the final bot

Bots will have a config file sitting somewhere that they need to
read from periodically. This file can be written to by brain_bot.
When brain_bot wants to put all the bots into telephone mode,
it will need to modify each bot's config file telling it which
order in the chain it belongs to, and which language it will be
synthesizing.

When in telephone mode, only bot_1 will listen for external speech.
After synthesizing speech, bot_1 will enter a "refractory period" of
90 seconds during which it won't listen to more speech. This prevents
multiple streams from traveling down the chain at one time.
"""

from flask import request


# Input languages (in order), requiring 4 bots.
LANGUAGES = ["English", "Spanish", "Japanese", "Turkish"]

# The ID's for each bot - probably a name like "botty" or "pi_3"
BOT_IDS = ["botty", "cam1", "cam2", "raspberry_pi"]

# Passwords - TODO: should be saved in a local file here
PASSWORDS = ["123", "password", "derp", "abcdefg"]


def setup_telephone_configs():
    """
    SSH into a bot, navigate to the correct folder, and then modify the config file
    """

    for id, password, lang in zip(BOT_IDS, PASSWORDS, LANGUAGES):
        # Use the id and password to SSH into the bot

        # Navigate to the correct folder

        # Read the config file

        # Write the new mode and language
        pass
    pass


def create_text_chain(text):
    """
    Translates whatever bot_1 heard into lang_2, then that into lang_3, etc
    """

    # Dummy data
    return ["hello, how are you?", "hola, como estas?", "こんにちは元気ですか", "Nasılsın?"]


"""
Needs to have a server running to listen for the transcription from bot_1
bot_1 only sends one transcription every 90 seconds

TODO: all the bots need to be refactored to operate as servers, as they will
sometimes need to talk to brain_bot
"""

# Track the current location on the chain. Global variable. This is OK.
current_bot_position = 1

@app.post('/start_chain')
def start_chain():
    # Listens for a post request from bot_1
    text = request.form["text"]

    # hard code the input text
    translation_chain = create_text_chain(text="hello, how are you?")
    
    # immediately send back the text to bot_1 to synthesize
    request.send(text[current_bot_position]) # not correct syntax...

    current_bot_position += 1
    
