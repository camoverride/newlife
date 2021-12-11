# newlife

## TODO

- add tests
- add proper module and function documentation


## Pi Setup - hardware


## Pi Setup - software

SSH into your pi, preferably with a proxy like [tailscale](https://tailscale.com/).

Suppress annoying "pop-up" noise:
`sudo mv /usr/share/piwiz/srprompt.wav /usr/share/piwiz/srprompt.wav.bak`

Clone repo:

`git clone https://github.com/camoverride/newlife.git`

Install python requirements:

`cd newlife &&& pip install -r requirements.txt`

Install system dependencies:

`sudo apt-get install gstreamer-1.0`

Add "cronjob" by adding the following line to `/etc/xdg/lxsession/LXDE-pi/autostart` so that the system turns on after rebooting ([source](https://raspberrypi.stackexchange.com/questions/127927/pygame-mixer-does-not-play-sound-when-started-in-cron)):

```
@/usr/bin /home/pi/newlife/start_chat.sh
```




## TTS - Text to Speech

Test it yourself directly:
`python TTS_DeepSpeech/native_client/python/client.py --model TTS_DeepSpeech/deepspeech-0.9.3-models.tflite --audio TTS_DeepSpeech/sound.wav`

