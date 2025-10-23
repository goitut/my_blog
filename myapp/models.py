from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Author(models.Model):
  """Model representing an author."""
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)

  def get_absolute_urls(self):
    """Returns the URL to access a particular author instance."""
    return reverse('author-detail', args=[str(self.id)])
  
  def __str__(self):
    """String for representing the Model object."""
    return f'{self.first_name} {self.last_name} '
  
class Blog(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  last_updated = models.DateTimeField(auto_now=True)
  is_published = models.BooleanField(default=False)

  class Meta:
    ordering = ['-date_posted']

  def __str__(self):
    return self.title
  
  @classmethod
  def published(cls):
    return cls.objects.filter(is_published=True)
  
  


