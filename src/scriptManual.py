from twython import Twython, TwythonError

APP_KEY = 'AWP9yh9U2HaPPDxtdzEkxllxg'
APP_SECRET = 'HlhxsHWqyYCs2QHSskwexrAAkXzxQUBNhIeMO6FIMlHbDmGLHl'
OAUTH_TOKEN = '2820782380-OANu0vi1fQoAO1BN7g3AdtCx21j2toIAsLFhkqu'
OAUTH_TOKEN_SECRET = 'fxuUy7rmE25by5WDknjSI80KB5dHhePMNZftTCogUC4ZR'


dead = raw_input ("Dead: ")
infected = raw_input("Infected: ")
observation =raw_input("Observation: ")


# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
#    user_timeline = twitter.get_user_timeline(screen_name='elEconomistaes')
    twitter.update_status(status='Dead: ' + dead + '\n' + 
        'Patients Infected: ' + infected + '\n' +
        'Patients under Observation: ' + observation)
#      tweets = twitter.get_home_timeline()
except TwythonError as e:
    print e
    sys.exit()

print "[+] Timeline updated..."


'''
for tweet in tweets:
    print "[+]" + tweet['text']
    print "@" + tweet['user']['screen_name']
'''