from django.db import models
from django.utils import timezone
# Create your models here.

class ChaiVerity(models.Model):
  CHAI_CHOICES = [
    ("ML", "MASALA"),
    ("GR", "GINGER"),
    ("PL", "PLAIN"),
    ("EL", "ELACHI"),
    ("LE", "LEMON")
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="chais/")
  date_added = models.DateTimeField(default=timezone.now())
  chai_type = models.CharField(choices=CHAI_CHOICES, max_length=2)
  
  def __str__(self):
    return self.name
  