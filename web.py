from __future__ import print_function
import web
import time
import os
import pychromecast

# Radio feed URLs gleaned from http://www.radiofeeds.co.uk/mp3.asp

urls = (
    '/stop', 'stop',
    '/play', 'play',
    '/play/(.*)', 'play',
    '/', 'home',
    '/img/(.*)', 'images'
)

chromecast_name = "Downstairs"

root_url = "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/nonuk/sbr_low/llnw/"
app = web.application(urls, globals())
render = web.template.render('templates/', base='base')

class home:
    def GET(self):
        return render.home('')

class play:
    def GET(self, station):
        if not station or station == "radio4":
            media_uri = "bbc_radio_fourfm.m3u8"
            station = "Radio 4"
        if station == "radio6":
            media_uri = "bbc_6music.m3u8"
            station = "Radio 6"
        cast =  pychromecast.get_chromecasts_as_dict().keys()
        cast = pychromecast.get_chromecast(friendly_name=chromecast_name)
        cast.wait()
        mc = cast.media_controller
        mc.play_media(root_url + media_uri, 'application/x-mpegURL')
        mc.pause()
        time.sleep(2)
        mc.play()
        return render.home('Playing ' + station)

class stop:
    def GET(self):
    	cast =  pychromecast.get_chromecasts_as_dict().keys()
    	cast = pychromecast.get_chromecast(friendly_name=chromecast_name)
    	cast.wait()
    	mc = cast.media_controller
    	mc.pause()
    	time.sleep(2)
    	mc.stop()
        return render.home('Stopping Chromecast')

class images:
    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension

        cType = {
            "png":"images/png",
            "jpg":"images/jpeg",
            "gif":"images/gif",
            "ico":"images/x-icon"            }

        if name in os.listdir('templates/img'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('templates/img/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()

if __name__ == "__main__":
    app.run()
