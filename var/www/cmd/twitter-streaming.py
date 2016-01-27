# http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import os

#Variables that contains the user credentials to access Twitter API 
import credentials
consumer_key        = credentials.twitter['consumerKey']
consumer_secret     = credentials.twitter['consumerSecret']
access_token        = credentials.twitter['accessToken']
access_token_secret = credentials.twitter['accessTokenSecret']

base_directory    = '/var/www/html/data/'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, filepath):
        self.output_directory = filepath
        os.system("mkdir -p %s"%(filepath))

        d = datetime.now()
        self.filename = d.strftime("%H.txt")
        self.fh = open(self.output_directory + self.filename, "a")

        self.tweetCount = 0
        self.errorCount = 0
        self.last = datetime.now()

    # Called for every new tweet on stream
    def on_data(self, data):
        self.fh.write(data)
        self.tweetCount += 1

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    output_directory = base_directory + datetime.now().strftime('%Y/%m/%d/')

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(output_directory)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby', 'csharp', 'fsharp'])