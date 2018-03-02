class UserComments:

    comments_list=[]

    def __init__(self,author,description):
        self.author=author
        self.description=description


    #method 
    def save_comment(self):
        UserComments.comments_list.append(self)


    def deleteComment(self):
        UserComments.comments_list.remove(self)    






