from django.test import TestCase

from custom_user.models import CustomUser
from books.models import Book


class CustomUserTestModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='Fedya')

    def test_username_verbos_name(self):
        custom_user = CustomUser.objects.get(id=self.user.id)
        field_label = custom_user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'name')

    def test_username_max_length(self):
        custom_user = CustomUser.objects.get(id=self.user.id)
        max_length = custom_user._meta.get_field('username').max_length
        self.assertEqual(max_length, 100)


class BooksTestModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(name='A Byte of Python', popularity=20)

    def test_book_name_verbos_name(self):
        book = Book.objects.get(id=self.book.id)
        field_label = book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'book_name')

    def test_book_name_max_length(self):
        book = Book.objects.get(id=self.book.id)
        max_length = book._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_have_user(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.user_id, None)
