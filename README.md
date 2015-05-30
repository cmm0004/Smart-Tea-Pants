# Smart-Tea-Pants
An experiment in Django and machine learning. 

So, I hate using Twitter, and this app does it for me. Predicts if a recent follower is a business, blogger, or individual and then does different things depending on the outcome. Businesses are ignored and not followed back because they use the oppurtunity to talk about their product on MY twitter. 

Smart-tea-pants does the follow-friday tweets, automatically engages with followers who are individuals, and refollows them.
It also advertises a couple times a week 

~85% correct in guessing a business from a blogger or individual. it has the most trouble on bloggers because they look so much like businesses, and some are. I figure, even if it gets it wrong sometimes, it probably won't embarass me nearly as much as a real human would.

### Plans for the future
* Sentiment analysis, to teach the bot what are appropriate things to retweet so that can be automated as well. 
* have it examine the language used by popular tea companies and be able to make its own 'original' tweets.

### Things to do
* Make more tests
* add more phrases
* clean up models
* consider documention
* refactor
* Hey, works on my box.
* make a script to do initial set up of training data.
