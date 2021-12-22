import urllib
import webbrowser
CALLBACK_URL_BASE = 'pythonista://'
url = "tweetbot://x-callback-url/post?"

def tweet(txt,cb=CALLBACK_URL_BASE):
        data = {
          'text': txt,
          'callback_url': cb
        }
        surl = url + urllib.urlencode(data)
        webbrowser.open(surl)
        print "Tweet Complete!"
    