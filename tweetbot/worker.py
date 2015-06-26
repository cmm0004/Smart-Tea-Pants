import os
import time
import tweepy
import datetime
from tweetbot.helpers.auth import API
from tweetbot.helpers.follower import Follower
from tweetbot.helpers.search import Search
from tweetbot.helpers.personalize import WeekDayAware
from tweetbot.models import User, TrainingData
from sklearn import tree

########
# CONSTANTS
########


def main():
    if 'HEROKU_CONSUMER_KEY' in os.environ:
        CONSUMER_KEY = os.environ['HEROKU_CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['HEROKU_CONSUMER_SECRET']
        ACCESS_TOKEN = os.environ['HEROKU_ACCESS_TOKEN']
        ACCESS_SECRET = os.environ['HEROKU_ACCESS_SECRET']

        twitter_api = API(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
    else:
        twitter_api = API()
    TWITTER_BOT = twitter_api.authenticate()
    
    did_ff = False
    ind_adv = False
    while True:
        ####create the needed API Objects
        searcher = Search(TWITTER_BOT)
        followers = Follower(TWITTER_BOT)
        classifier = tree.DecisionTreeClassifier()
        wda = WeekDayAware()

        #### check to see if theres a new follower to follow
        #if not already in users:

        
        if not User.objects.filter(user_id=followers.most_recent_id):

            ### add him to the users database. this fails on dupes

            user_id = followers.addToUsers()

            ### if adding was successful (new user)
            print(user_id)
            if user_id:
                ##retrive him from user database
                most_recent_user_object = User.objects.filter(user_id=user_id)
    
                ## set up the classifier with all the training data
                u = User
                td = TrainingData
                target = TrainingData.get_targets(td)
                data = TrainingData.get_data(td)
                classifier = classifier.fit(data, target)
                
                ## predict the class of the new user
                new_data_to_predict_on = User.get_data(u, user_data_query=most_recent_user_object)
                prediction = classifier.predict(new_data_to_predict_on)
               
                ### save the new prediction in the TrainingData database
                TrainingData.save_from_users(td, most_recent_user_object, classification=prediction[0])
                ### update the user with the prediction as well
                User.update_classification(u, user_id, prediction[0])
                print(most_recent_user_object[0].screen_name + ' is a ' + prediction[0])
                print('updated training data and user table')
                ## if it was a blogger or individual, tweet at them!
                if prediction[0] != 'business':
                    #fails on a NSFW name. also fails if already following.
                    followers.mention_new_follower()
                else:
                    print(most_recent_user_object[0].screen_name + ' is a ' + prediction[0] + ' , did not mention or follow')
            
            ##if the user was a dupe, we've already done this.
            else: 
                print('already following most recent')

        #probably dont need this extra check to see if we have already tweeted at this person.
        else:
            print("already saved this follower " + str(followers.most_recent) + ", did not mention.")

        #begin favoriting! Favorite no matter what.    
        statuses = searcher.get_statuses(query="#teasontheloose", count=5)
        
        try:
            for status in statuses:
                TWITTER_BOT.create_favorite(status.id)
        except tweepy.TweepError as e:
                print(e)
                print("favorite failed on status: " + str(status.id))
                print(datetime.datetime.now())


        statuses = searcher.get_statuses(query="@TeasontheLoose", count=5)
        
        try:
            for status in statuses:
                TWITTER_BOT.create_favorite(status.id)
        except tweepy.TweepError as e:
                print(e)
                print("favorite failed on status: " + str(status.id))
                print(datetime.datetime.now())
        # try:
        #     for status in statuses:
        #         if status.text.find('What up?'):
        #             TWITTER_BOT.update_status(status="@" + status.user.screen_name + " Holla!")
        # except tweepy.TweepError as e:
        #     print(e)
        #     print('failed to hollaback.')
        ####
        # advertise individual twice a week
        ####
        adv, adv_followup = wda.buy_individual_status()
        if adv and adv_followup and not ind_adv:
            try:
                TWITTER_BOT.update_status(status=adv)
                print('advertised individual')
            except tweepy.TweepError as e:
                print(e)
                print("failure to tweet individual advertisement")
                print(datetime.datetime.now())
            try:
                TWITTER_BOT.update_status(status=adv_followup)
            except tweepy.TweepError as e:
                print(e)
                print("failure to tweet individual advertisment followup")
                print(datetime.datetime.now())
            #did this once already
            ind_adv = True
        #change flag back on non adv days
        if (wda.today_int % 3) != 0:
            ind_adv = False


        ##follow friday shout-outs,
        # if its friday,
        # and we havent already done it:

        # if (wda.today_int == 4) and (not did_ff):
        #     followers.ff_tweet(wda=wda)
        #     did_ff = True
        # #reset if we've done ff on a non-friday
        # #so it will be ready next week
        # elif wda.today_int != 4:
        #     did_ff = False
        # ## done, wait and go again.
        print('done')
        time.sleep(1800)    

main()
        