#!/usr/bin/env python3.6

from comments import UserComments

def createComment(author,description):
    newComment=UserComments(author,description)
    return newComment

def saveComment(comment):
    comment.save_comment()


def delComment(comment):
    comment.deleteComment()

def showAllComments():
    return UserComments.displayComments()        

print("WELCOME TO HAPPYTOONS")





















# if __name__ == '__main__':

    # main()
