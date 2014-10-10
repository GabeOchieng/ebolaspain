from twython import Twython, TwythonError

APP_KEY = '***REMOVED***'
APP_SECRET = '***REMOVED***'
OAUTH_TOKEN = '***REMOVED***'
OAUTH_TOKEN_SECRET = '***REMOVED***'

status = ''

fd = open('data.dat','r')
line = fd.readline()

for d in line.split(";")[:-1]:
	status += d + '\n'
status += line.split(";")[-1]

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
#    user_timeline = twitter.get_user_timeline(screen_name='elEconomistaes')
    twitter.update_status(status=status)
#      tweets = twitter.get_home_timeline()
except TwythonError as e:
    print e
    sys.exit()

print "[+] Timeline updated..."
