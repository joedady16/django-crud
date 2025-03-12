from django.db import models
import datetime

# Create your models here.

class Dealer(models.Model):

    tpaCode = models.CharField(max_length=5, default="NNNNN")
    dealerNumber = models.CharField(max_length=20)
    dealerName = models.CharField(max_length=200)
    dealerAddress = models.CharField(max_length=200)
    dealerCity = models.CharField(max_length=50, default="Need City")
    dealerState = models.CharField(max_length=2)
    dealerZip = models.CharField(max_length=10)
    dealerPhone = models.CharField(max_length=12)
    dealerStatus = models.CharField(max_length=2, default='NS')


    def __str__(self):
        return self.dealerName