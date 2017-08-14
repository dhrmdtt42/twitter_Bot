Like	any	tweet	that	has	the	hashtag	‘#IOT’Twitter Bot Documentation


STEP A:      MAKE AN APP FOR THE TWITTER BOT

•	Create a new account at Twitter that will work as a bot. Then go to apps.twitter.com, sign-in with your new Twitter account and create a Twitter application. Give your app a name, description and put any URL in the website field. Agree to the developer terms and submit the form.

•	Once the Twitter app has been created, click Modify App Permissions under Application Settings and change the access level to Read, Write and Access Direct Messages.

•	Next switch to the Keys and Access Tokens tab and click the Create My Access Token button. Twitter will generate the Consumer Keys and Access tokens that we will need in a next step.

STEP B:  CONFIGURE YOUR TWITTER BOTS

•	Go to https://github.com/tweepy/tweepy to open the tweepy and install via command “ pip install tweepy “ in python shell to access the twitter API.

•	After installation of tweepy we import the tweepy in our python code and the  enter the Twitter Consumer Key, Consumer Secret, Access Token and Access Secret that were generated in the previous step in our python code.

STEP C:  LIST ALL THE FOLLOWERS

•	We have taken help from the tweepy Documentations the link is given http://tweepy.readthedocs.io/en/v3.5.0/api.html# 
We use the followers() method to list the all followers of the user in our python code. The code is
 print ('\nFollowers in Twitter\n')
for user in tweepy.Cursor(api.followers, screen_name="@mishraddev").items(10):
    print (user.screen_name)

STEP D:  LIST ALL THE FOLLOWING USERS

•	We used the friends() method to list all the following users in our python code. The code is 

print ('\nFollowing in Twitter\n')
for friend in tweepy.Cursor(api.friends).items(10):
    print (friend.screen_name)  

STEP E:  LIKE A TWEET ONCE	IT IS TWEETED	BY @BOLTIOT	

•	We used the timeline() method to Like	a tweet once it is tweeted by @boltiot  in our python code. The code is 

print("Like any tweet	that has the hashtag	‘#IOT’")
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


STEP E:  LIKE ANY TWEET THAT HAS THE HASHTAG ‘#IOT’

•	We used the favourite() method to Like	any tweet	that has the hashtag ‘#IOT’ in our python code. The code is 

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


                

