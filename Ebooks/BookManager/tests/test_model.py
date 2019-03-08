from django.test import TestCase
from ..models import Book

class BookTest(TestCase):
    """Test books model related transactions"""

    def setUp(self):
        Book.objects.create(
            title = 'Hunger Games',
            author = 'James Hogwarts',
            book_link = 'www.hg.com'
        )
        Book.objects.create(
            title = 'The Oasis',
            author = 'Burger Martins',
            book_link = 'www.to.com'
        )

    def test_book_author(self):
        book1 = Book.objects.get(title='Hunger Games')
        book2 = Book.objects.get(title='The Oasis')

        self.assertEqual(
            book1.get_book_author(), 'James Hogwarts'
        )

        self.assertEqual(
            book2.get_book_author(), 'Burger Martins'
        )
