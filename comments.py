class UserComments:
    comments_list =[]

    def __init__(self,author,description):
        self.author=author
        self.description =description
# add comment
    def saveComment (self):
        UserComments.comments_list.append(self)