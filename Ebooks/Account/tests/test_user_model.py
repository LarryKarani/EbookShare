from django.test import TestCase
from ..models import User

class UserTest(TestCase):
    """Test user model"""

    def setUp(self):
        User.objects.create(
            username = 'Larry',
            password = '6398litein',
            email = 'larry@gmail.com')
        User.objects.create(
            username = 'Kevin',
            password = '6398litein',
            email = 'kevin@gmail.com'
        )


    def test_user_email(self):
        kevin = User.objects.get(username='Kevin')
        larry = User.objects.get(username='Larry')

        self.assertEqual(kevin.get_email(), 'kevin@gmail.com')
        self.assertEqual(larry.get_email(), 'larry@gmail.com')