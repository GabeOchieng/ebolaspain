from twython import Twython, TwythonError
import datetime
import os

#Number of datafiles to publish
max_news = 2
#Hastag to append to the end
hashtag = "#ebola"

APP_KEY = '***REMOVED***'
APP_SECRET = '***REMOVED***'
OAUTH_TOKEN = '***REMOVED***'
OAUTH_TOKEN_SECRET = '***REMOVED***'


folder = os.path.dirname(os.path.realpath(__file__))
j = datetime.datetime.now()
st = ''

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

for i in range(1,max_news+1):
    p = os.path.join(folder,'db'+str(i)+'.txt')
    if os.path.exists(p):       
        fd = open(p,'r')
        st = fd.read() + "\n" + j.strftime('%d%b %H:%Mh') + " " + hashtag
        print len(st)
        print st
        #Update status
        try:
            twitter.update_status(status=st)
        except Exception,e:
            print str(e)
            exit()
        print "[+] Timeline %s updated succesfully..." % i
    else:
        break
