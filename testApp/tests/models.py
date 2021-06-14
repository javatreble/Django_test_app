from django.test import TestCase
from testApp.models import Author, Book


# https://docs.djangoproject.com/en/3.0/topics/testing/tools/#testcase

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        #  create one book and two authors.
        cls.book = Book.objects.create(title="The man in the high castle")
        cls.philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        cls.juliana = Author.objects.create(first_name="Juliana", last_name="Crain")

    # testing two related models
    def test_book_has_an_author(self):
        print('Running test_book_has_an_author()')
        # assign our authors to the book
        self.book.authors.set([self.philip.pk, self.juliana.pk]) #
        self.assertEqual(self.book.authors.count(), 2)
        # # Or assign the book to each author
        # philip.book_set.add(book)
        # juliana.book_set.add(book)
        # self.assertEqual(book.authors.count(), 2)

    # testing a model string representation.
    def test_model_str(self):
        print('Running test_model_str()')
        self.assertEqual(str(self.book), "The man in the high castle")
        self.assertEqual(str(self.philip), "Philip K. Dick")
