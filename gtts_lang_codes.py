"""
This module contains all the languages that google text to speech (GTTS) can synthesize.
It also contains a function to map between language code and language name, which is
required by the API.
"""

import re

codes = {
"af": "Afrikaans",
"ar": "Arabic",
"bg": "Bulgarian",
"bn": "Bengali",
"bs": "Bosnian",
"ca": "Catalan",
"cs": "Czech",
"cy": "Welsh",
"da": "Danish",
"de": "German",
"el": "Greek",
"en": "English",
"eo": "Esperanto",
"es": "Spanish",
"et": "Estonian",
"fi": "Finnish",
"fr": "French",
"gu": "Gujarati",
"hi": "Hindi",
"hr": "Croatian",
"hu": "Hungarian",
"hy": "Armenian",
"id": "Indonesian",
"is": "Icelandic",
"it": "Italian",
"ja": "Japanese",
"jw": "Javanese",
"km": "Khmer",
"kn": "Kannada",
"ko": "Korean",
"la": "Latin",
"lv": "Latvian",
"mk": "Macedonian",
"ml": "Malayalam",
"mr": "Marathi",
# "my": "Myanmar (Burmese)",
"my": "Burmese",
"ne": "Nepali",
"nl": "Dutch",
"no": "Norwegian",
"pl": "Polish",
"pt": "Portuguese",
"ro": "Romanian",
"ru": "Russian",
"si": "Sinhala",
"sk": "Slovak",
"sq": "Albanian",
"sr": "Serbian",
"su": "Sundanese",
"sv": "Swedish",
"sw": "Swahili",
"ta": "Tamil",
"te": "Telugu",
"th": "Thai",
"tl": "Filipino",
"tr": "Turkish",
"uk": "Ukrainian",
"ur": "Urdu",
"vi": "Vietnamese",
# "zh-CN": "Chinese",
"zh-TW": "Taiwanese",
"zh-CN": "Chinese"
}

# Inverse this so it's easier to read in
tts_lang_codes = {v: k for k, v in codes.items()}

def check_for_translation_change(transcription):
    """
    Converts some human input like "translate Spanish" to the correct language code like "es".

    Parameters
    ----------
    transcription : str
        Something a human said

    Returns
    -------
        The language code that corresponds to the language.
    """
    try: # TODO: handle error properly (messes up when weird text encoding)
        lang_options_regex = "|".join([i for i in codes.values()])
        regex = f"[Tt]ranslate ({lang_options_regex})"
        if re.match(regex, transcription):
            lang_code = transcription.split()[1]
            return tts_lang_codes[lang_code]

        return False
    except TypeError:
        return False
