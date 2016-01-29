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

base_directory    = os.environ['HOME'] + '/data/'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.fh = None
        self.__switch_active_file()

        self.tweetCount = 0
        self.errorCount = 0

    # Called for every new tweet on stream
    def on_data(self, data):
        self.fh.write(data)
        self.tweetCount += 1
        if datetime.now().hour != self.current_hour:
            self.__switch_active_file()

        return True

    def close(self):
        try:
            self.fh.close()
        except:
            # Log
            pass

    def on_error(self, status):
        print(status)
        self.errorCount += 1

    # Determine directory, create it if it does not exist, close old file, create/open new file
    def __switch_active_file(self):
        d = datetime.now()

        self.current_hour = d.hour
        self.output_directory = self.base_directory + d.strftime('%Y/%m/%d/')
        os.system("mkdir -p %s"%(self.output_directory))

        if self.fh is not None:
            self.fh.close()
        self.filename = d.strftime("%H.txt")
        self.fh = open(self.output_directory + self.filename, "a")


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(base_directory)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby', 'csharp', 'fsharp'])