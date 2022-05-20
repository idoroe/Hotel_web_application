from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user','room','display','checkin','checkout','booking_code','no_days','amount','paid','available','checkout_update','future']
    readonly_fields = ['user','room','checkin','checkout','booking_code','no_days','amount','paid','available']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','amount','paid','phone','pay_code','payment_date','admin_update','admin_update','admin_note']
    readonly_fields =  ['user','first_name','last_name','amount','paid','phone','pay_code',]
