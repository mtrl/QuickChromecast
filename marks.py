from __future__ import print_function
import time
import pychromecast
cast =  pychromecast.get_chromecasts_as_dict().keys()
#cast = pychromecast.get_chromecast()
cast = pychromecast.get_chromecast(friendly_name="Kitchen")
cast.wait()
mc = cast.media_controller
mc.play_media('http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_med/llnw/bbc_radio_fourfm.m3u8', 'application/x-mpegURL')
#mc.play_media('http://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3', 'audio/mpeg')
print(mc.status)
mc.pause()
time.sleep(2)
mc.play()
mc.stop()
