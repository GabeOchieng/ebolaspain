from twython import Twython, TwythonError
import sys
import datetime

i = datetime.datetime.now()

APP_KEY = '***REMOVED***'
APP_SECRET = '***REMOVED***'
OAUTH_TOKEN = '***REMOVED***'
OAUTH_TOKEN_SECRET = '***REMOVED***'

status = ''

fd = open('db.txt','r')
status = i.strftime('%d%b %H:%Mh') + "\n" + fd.read() + "\n#ebola"
print len(status)

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
#    user_timeline = twitter.get_user_timeline(screen_name='elEconomistaes')
    twitter.update_status(status=status)
#      tweets = twitter.get_home_timeline()
except TwythonError as e:
    print e
    sys.exit()

print "[+] Timeline updated succesfully..."
