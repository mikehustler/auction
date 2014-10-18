from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    prov = models.CharField(max_length=50)
    pc = models.CharField(max_length=9)
    def __str__(self):
        return self.street


class RegisteredPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address)
    def __str__(self):
        return self.last_name + ", " + self.first_name


class AuctionItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    fmv = models.DecimalField('fair market value', max_digits=7, decimal_places=2)
    opening_bid = models.DecimalField('fair market value', max_digits=7, decimal_places=2)
    donor = models.ForeignKey(RegisteredPerson)

