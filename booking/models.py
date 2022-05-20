from re import T
from django.db import models
from django.contrib.auth.models import User
from room.models import Room
from django.utils import timezone
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    booking_code = models.CharField(max_length=50)
    checkin = models.DateField()
    checkout = models.DateField()
    no_days = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(default=1)
    amount = models.IntegerField(blank=True,null=True)
    paid = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    booking_date = models.DateTimeField(auto_now=True)
    del_booking = models.DateTimeField(default=timezone.now)
    future = models.BooleanField(default=False)
    checkout_update = models.DateTimeField(auto_now=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    phone = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=36)
    booking_code = models.CharField(max_length=36)
    payment_date = models.DateTimeField(auto_now=True)
    admin_update = models.DateTimeField(auto_now=True)
    admin_update = models.DateTimeField(auto_now=True)
    admin_note = models.TextField(blank=True,null=True)

    


    def __str__(self):
        return self.user.username
    