from SocialMedia import SocialMedia

class instagram (SocialMedia):

    def __init__(self,posts):
       self.posts = posts

    def publishNewPost(body):

        Posts = []
       

        if(len(body)<2200):

            Posts.append(body)

            print(Posts)
        
        else :
            print("your post haven't passed the rules")

    def getPosts(self):
        return self.posts


    body = input("Write your caption (post) :")

    p = publishNewPost(body)



