from django.db import models
from dgango.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length = 255)
    created_at = madels.DateTimeField(default=timezone.now)

class Course(models.Model):
    title = models.CharField(max_length = 255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = madels.DateTimeField(default=timezone.now)

