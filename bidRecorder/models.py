from django.db import models


class Auction(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    prov = models.CharField(max_length=50)
    pc = models.CharField(max_length=9)
    def __str__(self):
        return self.street


class Registrant(models.Model):
    auction = models.ForeignKey(Auction)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address)
    def __str__(self):
        return self.last_name + ", " + self.first_name


class AuctionItem(models.Model):
    auction = models.ForeignKey(Auction)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    fmv = models.DecimalField('fair market value', max_digits=7, decimal_places=2)
    opening_bid = models.DecimalField('fair market value', max_digits=7, decimal_places=2)
    donor = models.ForeignKey(Registrant)
    def __str__(self):
        return self.name
