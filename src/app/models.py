from django.db import models

# Create your models here.
class person(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    salary=models.IntegerField()

    def __str__(self):
        return self.name
    