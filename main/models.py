from django.db import models
import uuid

class Item(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    animal_type = models.CharField(max_length=255)
    stock = models.IntegerField()