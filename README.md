# newlife 🤖

This is a hardware/software project that brings intelligent agents to your home! Newlife is like Amazon Echo or Google Home but hackable and less creepy 😱


## Pi Setup - hardware

WIP


## Pi Setup - software

ssh into your pi, preferably with a proxy like [tailscale](https://tailscale.com/).

Suppress annoying "pop-up" noise:
`sudo mv /usr/share/piwiz/srprompt.wav /usr/share/piwiz/srprompt.wav.bak`

Clone repo:

`git clone https://github.com/camoverride/newlife.git`

Install python requirements:

`cd newlife && pip install -r requirements.txt`

Install system dependencies:

`sudo apt-get install gstreamer-1.0`

Add "cronjob" by adding the following line to `/etc/xdg/lxsession/LXDE-pi/autostart` so that the system turns on after rebooting ([source](https://raspberrypi.stackexchange.com/questions/127927/pygame-mixer-does-not-play-sound-when-started-in-cron)):

```
@/usr/bin /home/pi/newlife/start_chat.sh
```

If you want to start the python script manually while ssh'd into your Pi but don't want it to shut down when you log out, use `nohup` and check `nohup.out` for logs:

`nohup python chat.py &`


## How to use 🔊

You have to talk to Newlife to make it work 💬. Newlife has modes: _chat_, _echo_, and _translate_. To switch between modes, simply say "mode translate" etc. _chat_ is a generic chat mode that you can hack, _echo_ repeats back to you whatever you say, and _translate_ repeats back to you whatever you say but in a different language!

Newlife can speak in multiple languages 🇷🇺. To switch between these say "translate Japanese." If Newlife is in echo mode but is set to "translate Japanese" (or any other language) it will echo back your words in a Japanese accent.

Newlife has multiple Personas. Personas are the background information about the bot: its age, feelings, and disposition. These can't be changed on the fly but can be accessed in `chat.py` and are defined in `personas.py`.


## Beneath the hood

There are three main stages in the AI process: collect speech from a human, figure out a response, and speak the response. These stages are called Automatic Speech Recognition or ASR 👂, knowledge (my term) 🧠, and Text to Speech or TTS 🗣️. These phases can further be sub-divided:

- ASR 👂
    - Determine which segment of audio corresponds to a speech signal (vs random noise)
    - Determine whether to incrementally process speech signal or process all at once

- Knowledge 🧠
    - Check which mode we're in (chat, echo, translate)
    - Consider whether to use a pre-determined reply or create one fresh

- TTS 🗣️
    - Check whether the response has been cached or if a model needs to be called.
    - Determine whether to process the entire speech signal at once or chop it up.

Furthermore, each of these stages can be augmented by different machine learning models. ASR involves creating features from text (mel's), applying a model to predict the phoneme each feature corresponds to, decoding these into words, and then applying a language model to test the plausibility of different sentences. Knowledge generation is a combination of rules and machine learning: when a response isn't known, one can be generated automatically with a language model like GPT3, but this requires careful encoding and decoding of data. Text to speech can likewise be divided between pre-computed and on-the-fly tasks.


## TODO

- add tests
- add custom voice options
- add more personas
- use gpt to generate responses in chat mode
