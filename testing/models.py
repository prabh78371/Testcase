from audioop import reverse
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    reg_number = models.CharField(max_length=30)
    date_of_admission = models.DateField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
    

    def __str__(self):
        return f"name:{self.first_name} {self.last_name} {self.reg_number}"