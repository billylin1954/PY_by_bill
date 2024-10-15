from django.db import models
class flights(models.Model):
    start=models.CharField(max_length=64)
    end=models.CharField(max_length=64)
    time=models.IntegerField()
    def __str__(self):
        return f"{self.id}:{self.start} to {self.end}"
