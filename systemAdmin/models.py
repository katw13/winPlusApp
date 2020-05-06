from django.db import models

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=40, blank= False)
    cost = models.CharField(max_length=40, blank= False)
    
    def __str__(self):
        return self.name + '--'+ self.cost 

class token(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    tokenNumber = models.CharField(max_length=40, blank= False)
    winAmount = models.CharField(max_length=40, blank= False)
    winActivation = models.CharField(max_length=40, blank= False)
    currentInUse = models.BooleanField(null=True, blank= True)
    
    def __str__(self):
        return self.tokenNumber + '--'+ self.package.name + '--' + self.winAmount + '--'+ self.winActivation

class promotionOffer(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    region = models.CharField(max_length=40, blank= False)

    def __str__(self):
        return self.package.name + '--' + self.region 


