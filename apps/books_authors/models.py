from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):                                  #displays the information in the terminal!
        return "first:: {} desc:: {}".format(self.name,self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField(default = '')
    def __repr__(self):                             #displays the information in the terminal!
        return "first:: {} last:: {} email:: {} books:: {} notes {}".format(self.first_name,self.last_name,self.email,self.books,self.notes)



