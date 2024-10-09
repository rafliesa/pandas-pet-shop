from django.db import models
import uuid
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Item(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(100)])
    description = models.TextField()
    animal_type = models.CharField(max_length=255)
    stock = models.IntegerField(validators=[MinValueValidator(0)])