import tweepy
from time import sleep
consumer_key='VoF1lrTZ5T4BfjMcK861s47I3'
consumer_secret='0OaDud4bzECy4VPY8EdQTxbJztTxjR5LW4VavqE5lbIjgr6MPE'
access_token='864148006890819588-aSrlvpS1LSVRIKn2kHTrsxVjQwS7UR9'
access_token_secret='aPZyPfxfdszDvNa8oJkB5yyyQNuifwaBigad5aYRwWxGo'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth,wait_on_rate_limit=True)
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
for user in tweepy.Cursor(api.followers, screen_name="@mishraddev").items(10):
    print (user.screen_name)

## To print names of people whom I am following
print ('\nFollowing in Twitter\n')
for friend in tweepy.Cursor(api.friends).items(10):
    print (friend.screen_name) 
print("Like	any	tweet	that	has	the	hashtag	‘#IOT’")
	#for favorite in tweepy.Cursor(api.favorite,q='#IOT').items(10):
	#    print(favorite.screen_name)
tweet=api.user_timeline(screen_name="@GregoriaTravels",count=1)
#for t in tweet:
  #  try:
      #  if t.favorited==False:
       #     t.favorite()
        #if t.favorited==True:
         #   break
for tw in tweepy.Cursor(api.search,q='#IoT').items(10): 
    if tw.favorited==False:
        tw.favorite()
        
