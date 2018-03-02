from comments import UserComments
import unittest


class TestComment(unittest.TestCase):
    def setUp(self):
        self.comment =UserComments("collins","my first comment")

    def tearDown(self):
        UserComments.comments_list=[]

    def test_initialize_comments(self):
        self.assertEqual(self.comment.author,"collins")
        self.assertEqual(self.comment.description,"my first comment")
        
    def test_save_comment(self):
        self.comment.saveComment()
        self.assertEqual(len(UserComments.comments_list),1)

    # def test_update_comment(self):
        # self.comment.editComment()
        # self.comment.savecomment()
        # self.assertEqual((UserComments.comments_list.description),"newcomment")


