class UserComments:
    comments_list =[]

    def __init__(self,author,description):
        self.author=author
        self.description =description
# add comment
    def saveComment (self):
        UserComments.comments_list.append(self)

    # def editComment (self,newcomment,oldcomment):
    #     for comment in UserComments.comments_list:
    #         if comment.description == oldcomment:
    #             comment.description.replace(oldcomment,newcomment)
    #             return newcomment


    