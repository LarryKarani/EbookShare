from django.db import models

# Create your models here.
class Book(models.Model):
    """
    Defines the attributes of a book
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_link = models.CharField(max_length=255)
    posted_on = models.DateField(auto_now_add=True)
    #posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_book_author(self):
        return self.author

    def __repr__(self):
        return self.title

