from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "TWITTER_CONSUMER_KEY"
consumer_secret = "TWITTER_CONSUMER_SECRET"

access_token = "TWITTER_APP_ACCESS_TOKEN"
access_token_secret = "TWITTER_APP_TOKEN_SECRET"

class StdOutListener(StreamListener):
	""" A listener handles tweets that are received from the stream
	This is a basic listener that just prints the received tweets to stdout."""

	def on_data(self, data):
		print(data)
		return True


	def on_error(self, status):
		print(status)
		if status == 420:
			# returning False disconnects the stream to avoid rate limiting
			return False


if __name__ == "__main__":
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)
	stream.filter(track=['@realDonaldTrump'], async=True)
