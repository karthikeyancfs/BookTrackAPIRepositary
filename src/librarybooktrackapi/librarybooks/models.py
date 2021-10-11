from django.db import models

# Create your models here.

class library(models.Model):
    library_name  = models.CharField(max_length=50, null='true', blank='true')
    city  = models.CharField(max_length=50, null='true', blank='true')
    state  = models.CharField(max_length=50, null='true', blank='true')
    postal_code  = models.CharField(max_length=50, null='true', blank='true')

    def __str__(self):
        return self.library_name

    def __unicode__(self):
        return self.library_name
    
    class Meta:
        verbose_name        = "Library"
        verbose_name_plural = "Libraries"

class book(models.Model):
    title  = models.CharField(max_length=100, null='true', blank='true')
    author_name  = models.CharField(max_length=50, null='true', blank='true')
    isbn_num  = models.CharField(max_length=50, null='true', blank='true')
    genre  = models.CharField(max_length=50, null='true', blank='true')
    description = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name        = "Book"
        verbose_name_plural = "Books"

class library_user(models.Model):
    name  = models.CharField(max_length=100, null='true', blank='true')
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "User"
        verbose_name_plural = "Users"


class library_book(models.Model):
    library = models.ForeignKey(library, on_delete=models.CASCADE, related_name='library_book_library_name', blank=True, null=True)
    book = models.ForeignKey(book, on_delete=models.CASCADE, related_name='library_book_title', blank=True, null=True)
    activity_id = models.IntegerField(verbose_name = 'Last activity ID', blank=True, null=True)

    def __str__(self):
        return self.book.title

    def __unicode__(self):
        return self.book.title
    
    class Meta:
        verbose_name        = "Library Book"
        verbose_name_plural = "Library Books"

class library_activity(models.Model):
    activity_type = models.CharField(max_length=255, blank=True, null=True, default = "checked_in", choices = [('checked_in', 'checked_in'), ('checked_out', 'checked_out')])
    library_user = models.ForeignKey(library_user, on_delete=models.CASCADE, related_name='library_activity_users', blank=True, null=True)
    library_book = models.ForeignKey(library_book, on_delete=models.CASCADE, related_name='library_books',blank=True, null=True)
    checked_out_at = models.DateTimeField(blank=True, null=True)
    checked_in_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.library_user.name

    def __unicode__(self):
        return self.library_user.name
    
    class Meta:
        verbose_name        = "Library activity"
        verbose_name_plural = "Library activities"