import tweepy

class Follower(object):
    def __init__(self, TWITTER_BOT):
        self.TWITTER_BOT = TWITTER_BOT
        self.followers = self.TWITTER_BOT.followers()
        self.most_recent = self.followers[0].screen_name

    def _follow_most_recent(self):
        if self._check_name_nsfw():
            print 'nsfw name didnt follow'
            return
        else:
            self.TWITTER_BOT.create_friendship(screen_name=self.most_recent)

    def _am_following(self):
        friendship = self.TWITTER_BOT.show_friendship(source_screen_name='TeasontheLoose', target_screen_name=self.most_recent)
        #check if friendship[0].following or friendship[0].following_requested are true
        if friendship[0].following:
            return friendship[0].following
        elif friendship[0].following_requested:
            return friendship[0].following_requested
        return False
                                                 
    def mention_new_follower(self):
        am_following = self._am_following()

        if self._check_name_nsfw():
            print "nsfw name, didnt mention"
            return       

        #if not already following the most recent follower:

        if not am_following:
            lines = open("./fixtures/msgs_to_followers.txt").read().splitlines()
            mention = "@" + str(self.most_recent)
            try:
                self.TWITTER_BOT.update_status(mention + " " + random.choice(lines))
                print "successfully mentioned new follower: " + str(self.most_recent), datetime.datetime.now()
                self._follow_most_recent()
                print "followed new follower " + str(self.most_recent), datetime.datetime.now()
                
            except tweepy.TweepError:
                print "mention failed on new follower " + self.most_recent
                print datetime.datetime.now()
        else:
            print "already following " + str(self.most_recent) + ", did not mention."
            
    def poach_followers(self, target, number):
        targets_followers = self.TWITTER_BOT.followers(screen_name=target, count=number)
        for follower in targets_followers:
            try:
                self.TWITTER_BOT.create_friendship(screen_name=follower.screen_name)
                print "followed new follower " + str(follower.screen_name), datetime.datetime.now()
            except tweepy.TweepError:
                print 'error, didn\'t follow ' + str(follower.screen_name), datetime.datetime.now()
    
    def _check_name_nsfw(self):
        name = str(self.most_recent)
        uppercase_name = name.upper()
        pattern = re.compile("FUCK|DAMN|SHIT|PUSSY|PENIS|COCK|VAGINA|MOTHERFUCK|PISS|FAGGOT")
        match = pattern.search(name)

        return not not match
