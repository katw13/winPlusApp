from django.db import models

# Create your models here.
class CustomerData(models.Model):
    firstName = models.CharField(max_length=300, blank= False)
    lastName = models.CharField(max_length=300, blank= False)
    password = models.CharField(max_length=3000, blank= False)
    email = models.EmailField(max_length=200, blank=True)
    phoneNumber=models.CharField(max_length= 40, blank=False)
    
    def __str__(self):
        return self.firstName  + '--'+ self.lastName + '--'+ self.email + '--'+ self.phoneNumber


