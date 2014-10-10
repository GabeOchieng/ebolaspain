from twython import Twython, TwythonError
import sys
import datetime

i = datetime.datetime.now()

APP_KEY = 'AWP9yh9U2HaPPDxtdzEkxllxg'
APP_SECRET = 'HlhxsHWqyYCs2QHSskwexrAAkXzxQUBNhIeMO6FIMlHbDmGLHl'
OAUTH_TOKEN = '2820782380-OANu0vi1fQoAO1BN7g3AdtCx21j2toIAsLFhkqu'
OAUTH_TOKEN_SECRET = 'fxuUy7rmE25by5WDknjSI80KB5dHhePMNZftTCogUC4ZR'

status = ''

fd = open('db.txt','r')
status = fd.read() + "\n" + i.strftime('%d%b %H:%Mh') + " #ebola"
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
