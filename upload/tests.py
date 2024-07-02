from django.test import TestCase
from .models import Post


class PostTests(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(
            title="just a test", author="Arinze", slug="arinze-test"
        )
        self.blog.save()

    def test_post_content(self):
        self.assertEqual(self.blog.title, "just a test")
        self.assertEqual(self.blog.author, "Arinze")
        self.assertEqual(self.blog.slug, "arinze-test")
        self.assertEqual(str(self.blog), "just a test")
