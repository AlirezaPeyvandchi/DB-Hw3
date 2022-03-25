from SocialMedia import SocialMedia

class twitter (SocialMedia):

    def __init__(self,tweets):
       self.tweets = tweets

    def createNewTweet(body):

        Tweets = []
       

        if(len(body)<280):

            Tweets.append(body)

            print(Tweets)
        
        else :
            print("your post haven't passed the rules")

    def getTweets(self):
        return self.tweets


    body = input("Write your tweet :")

    p = createNewTweet(body)



