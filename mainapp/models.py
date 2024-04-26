import datetime
from django.forms import ModelForm
from django.db import models
from django.utils.timezone import datetime


class Event(models.Model):
    event_name=models.CharField(max_length=500,null=True,blank=True)
    event_description=models.TextField(max_length=500,null=True,blank=True)
    event_venue=models.CharField(max_length=500,null=True,blank=True)
    event_start_date=models.DateTimeField(default=datetime.now, blank=True)
    event_end_date=models.DateTimeField(default=datetime.now, blank=True)
    event_image = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.event_name



class Tickets(models.Model):
    ticket_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    ticket_name= models.CharField(max_length=50,null=True,blank=True)
    max_count=models.PositiveIntegerField(default=0)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_percentage=models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField()
    open_time_date=models.DateTimeField(default=datetime.now, blank=True)
    close_time_date=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.ticket_id
    





