from django.db import models
from datetime import datetime, date


class DayPlan(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    is_rest = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class PlanCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Plan Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class FitnessPlan(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=80)
    plan_category = models.ForeignKey('PlanCategory', null=True, blank=True, on_delete=models.SET_NULL)
    start_day = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    day_one = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)
    day_two = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)
    day_three = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)
    day_four = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)
    day_five = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)
    day_six = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)
    day_seven = models.ForeignKey('DayPlan', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
