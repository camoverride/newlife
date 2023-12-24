# Translator

Translates to a language of your choice!


## Pi Setup

- `git clone https://github.com/camoverride/newlife.git`
- `cd newlife`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `sudo apt-get install flac`

Suppress annoying "pop-up" noise:
`sudo mv /usr/share/piwiz/srprompt.wav /usr/share/piwiz/srprompt.wav.bak`


## Run

`nohup python translate_bot.py &`


## How to use

The bot listens to your speech and repeats it back, translated into a new language.

To switch languages, simply say "translate Chinese." A full list of languages is in `gtts_lang_codes.py`
