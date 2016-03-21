from __future__ import print_function
import web
import time
import pychromecast
        
urls = (
    '/stop', 'stop',
    '/play', 'play',
    '/', 'play'
)
app = web.application(urls, globals())

class play:
    def GET(self):
	cast =  pychromecast.get_chromecasts_as_dict().keys()
	cast = pychromecast.get_chromecast(friendly_name="Downstairs")
	cast.wait()
	mc = cast.media_controller
	mc.play_media('http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/nonuk/sbr_vlow/llnw/bbc_radio_fourfm.m3u8', 'application/x-mpegURL')
	mc.pause()
	time.sleep(2)
	mc.play()
        return 'Playing BBC Radio 4'

class stop:
    def GET(self):
	cast =  pychromecast.get_chromecasts_as_dict().keys()
	cast = pychromecast.get_chromecast(friendly_name="Downstairs")
	cast.wait()
	mc = cast.media_controller
	mc.pause()
	time.sleep(2)
	mc.stop()
        return 'Stopping BBC Radio 4'

if __name__ == "__main__":
    app.run()
