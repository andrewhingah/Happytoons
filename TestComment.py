from comments import UserComments

import unittest


class TestComment(unittest.TestCase):

    def setUp(self):
        self.comment=UserComments("collins","my first comment")

    def test_initialize_comment(self):
        self.assertEqual(self.comment.author,"collins")
        self.assertEqual(self.comment.description,"my first comment")

    def test_save_comment(self):
        self.comment.save_comment()
        self.assertEqual(len(UserComments.comments_list),1)        
