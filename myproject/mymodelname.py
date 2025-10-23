from django.db import models
from django.urls import reverse

class mymodelnamepypy(models.Model):
  """A typical class defining a model,derived from the model class."""

  # Fields 
  my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
  # ...

  # Metadata
  class Meta:
    ordering = ['-my_field_name']

  # Methods 
  def get_absolute_urls(self):
    """Returns the URL to access a particular instance of mymodelname."""
    return reverse('model-detail-view', args=[str(self.id)])
  
    def __str__(self):
      """String for representing the mymodelname object (in Admin site etc.)"""
      return self.my_field_name