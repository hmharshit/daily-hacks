"""This script tweets random motivational quotes on your twitter account"""

import requests
import datetime
import tweepy

# Update the credentials of your a/c. Refer here to make app https://apps.twitter.com
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

API = 'https://talaikis.com/api/quotes/random/'

curr_day = datetime.datetime.now().weekday()
day = ['MondayMotivation', 'TuesdayThoughts', 'WednesdayWisdom', 'ThursdayMotivation',
       'FridayFeeling', 'SaturdayThinking', 'SundayMorning']  # Trending hashtags

response = requests.get(api).json()
quote = response.get('quote') + '\n#{}'.format(day[curr_day])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(status=quote)
