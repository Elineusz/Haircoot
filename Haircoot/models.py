from django.db import models
from django.contrib.auth.models import User


class Selections(models.Model):
    selection_name = models.CharField(max_length=200)
    selection_choices = models.CharField(max_length=200)


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_detailed = models.TextField()
    service_duration = models.DurationField()
    service_price = models.FloatField()


class Reservation(models.Model):
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.SET_NULL, null=True)
    customer_first_name = models.CharField(max_length=100, null=True)
    customer_surname = models.CharField(max_length=200, null=True)
    customer_phone_prefix = models.IntegerField(null=True)
    customer_phone = models.IntegerField(null=True)
    customer_email = models.EmailField(null=True)
    chosen_service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    service_cost = models.FloatField()
    reservation_start = models.DateTimeField
    reservation_end = models.DateTimeField
    employee = models.ForeignKey(User, related_name='employee', on_delete=models.SET_NULL, null=True)


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_prefix = models.IntegerField()
    phone = models.IntegerField()
    # discount = models.IntegerField()
    # discount_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class EmployeeSkills(models.Model):
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

#
# class Calendar:
#     customer = models.ForeignKey(User, on_delete=models.PROTECT())
#     employee = models.ForeignKey(User, on_delete=models.PROTECT())
#     service = models.ManyToManyField(Service)
