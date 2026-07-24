from django.urls import path
from .views import MealPlanListView, MealSubscriptionListCreateView

urlpatterns = [
    path('plans/', MealPlanListView.as_view(), name='meal_plan_list'),
    path('subscriptions/', MealSubscriptionListCreateView.as_view(), name='meal_subscription_list_create'),
]
