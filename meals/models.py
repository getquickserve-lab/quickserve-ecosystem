from django.db import models
from django.conf import settings
class MealPlan(models.Model):
    name = models.CharField(max_length=20, unique=True)
    weekly_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
class MealSubscription(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meal_subscriptions')
    plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    selected_meals_json = models.JSONField()
