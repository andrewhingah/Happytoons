from comments import UserComments

import unittest


class TestComment(unittest.TestCase):

    def setUp(self):
        self.comment=UserComments("collins","my first comment")


    def tearDown(self):
        UserComments.comments_list=[]    

    def test_initialize_comment(self):
        self.assertEqual(self.comment.author,"collins")
        self.assertEqual(self.comment.description,"my first comment")

    def test_save_comment(self):
        self.comment.save_comment()
        self.assertEqual(len(UserComments.comments_list),1)

    def test_many_comments(self):
        self.comment.save_comment()
        self.test_comment=UserComments("mike","good place")
        self.test_comment.save_comment()
        self.assertEqual(len(UserComments.comments_list),2)


    def test_delete_comment(self):
        self.comment.save_comment()
        self.test_comment=UserComments("mike","good place")
        self.test_comment.save_comment()
        self.test_comment.deleteComment()
        self.assertEqual(len(UserComments.comments_list),1)  



    def test_show_comments(self):
        self.assertEqual(UserComments.displayComments(),UserComments.comments_list)     

                    
