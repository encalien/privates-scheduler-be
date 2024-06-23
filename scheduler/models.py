from django.db import models
from django.utils.translation import gettext_lazy as _


class Priority(models.IntegerChoices):
    GREEN = 1, _("Green")
    YELLOW = 2, _("Yellow")
    RED = 3, _("Red")


class Status(models.IntegerChoices):
    OPEN = 1, _("Open")
    BOOKED = 2, _("Booked")
    CONFIRMED = 3, _("Confirmed")


# Create your models here.


class Customer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TimeSlot(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.PositiveIntegerField(choices=Priority, default=Priority.YELLOW)
    status = models.PositiveIntegerField(choices=Status, default=Status.OPEN)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"

    def set_priority(self, new_priority):
        self.priority = new_priority
        self.save()

    def book(self, customer):
        self.customer = customer
        self.status = 2
        self.save()
