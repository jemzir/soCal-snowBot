import tweepy
import config

# client = tweepy.Client(consumer_key=config.API_KEY,
#                        consumer_secret=config.API_SECRET,
#                        access_token=config.ACCESS_TOKEN,
#                        access_token_secret=config.ACCESS_TOKEN_SECRET)

# response = client.create_tweet()

def api():
  auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
  auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

  return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
  api.update_status(message)
  print('Tweet success!')

api = api()
tweet(api, 'E&J tweeting from Python!')

# import in tweetpy
# https://www.youtube.com/watch?v=2UBcRiddwAo <-- use this vid

# import in the keys in a file that will be ignored on git pushes


# create an Oauth  with the access tokens and secrets

# define a tweet function that will invoke tweet posts
