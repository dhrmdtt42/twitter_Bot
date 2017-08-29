import tweepy
from time import sleep
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
    print ('\nFollowing in Twitter\n')
for friend in tweepy.Cursor(api.friends).items(10):
    print (friend.screen_name) 
print("Like	any	tweet	that	has	the	hashtag	‘#IOT’")
tweet=api.user_timeline(screen_name="@GregoriaTravels",count=1)
for t in tweet:
    try:
        if t.favorited==False:
            t.favorite()
        if t.favorited==True:
            break
    except tweepy.TweepError as e:
            print(e.reason)
            sleep(10)
            continue
    except StopIteration:
            break
print("Like a tweet once it  is tweeted  by @boltiot")
for tw in tweepy.Cursor(api.search,q='#IoT').items(10): 
    try:
        if tw.favorited==False:
           tw.favorite()
        if tw.favorited==True:
           break
    except tweepy.TweepError as e:
               print(e.reason)
               sleep(10)
               continue
    except StopIteration:
               break

