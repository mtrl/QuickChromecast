# Quickcast

One touch playing of media to a Chromecast :)

Run this python script on a raspberrypi or similar and save the web page as a shortcut on your mobile device.

1. Install web.py
```
git clone git://github.com/webpy/webpy.git
ln -s `pwd`/webpy/web .
```
2. pip install -r requirements
2. Change chromecast_name in web.py to your Chromecast or group name
3. ```nohup python quick_chromecast.py &```
4. Access your quickcast app
5. Save time and profit!
