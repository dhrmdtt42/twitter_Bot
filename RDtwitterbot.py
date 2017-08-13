import tweepy
from time import sleep
consumer_key='VoF1lrTZ5T4BfjMcK861s47I3'
consumer_secret='0OaDud4bzECy4VPY8EdQTxbJztTxjR5LW4VavqE5lbIjgr6MPE'
access_token='864148006890819588-aSrlvpS1LSVRIKn2kHTrsxVjQwS7UR9'
access_token_secret='aPZyPfxfdszDvNa8oJkB5yyyQNuifwaBigad5aYRwWxGo'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)
myBot = api.get_user(screen_name='@mishraddev')
"""
for tweet in tweepy.Cursor(api.search, q='@mishraddev').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.retweet()
        print('Retweeted the tweet')
        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')
        # Follow the user who tweeted
        tweet.user.follow()
        print('Followed the user')
        sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(10)
        continue
    except StopIteration:
        break
                
   """

print ('\nFollowers in Twitter\n')
for number_of_user in tweepy.Cursor(api.followers, screen_name="@mishraddev").items():
    print (number_of_user.screen_name)

## To print names of people whom I am following
#Code snippet taken from http://docs.tweepy.org/en/v3.5.0/code_snippet.html
print ('\nFollowing in Twitter\n')
for friend in tweepy.Cursor(api.friends).items():
	print (friend.screen_name)   
        
