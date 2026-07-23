from django.contrib import admin
from .models import MealPlan, MealSubscription
admin.site.register([MealPlan, MealSubscription])
