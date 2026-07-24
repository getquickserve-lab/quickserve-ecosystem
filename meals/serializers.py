from rest_framework import serializers
from .models import MealPlan, MealSubscription

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ('id', 'name', 'weekly_price', 'description')

class MealSubscriptionSerializer(serializers.ModelSerializer):
    plan_name = serializers.ReadOnlyField(source='plan.name')

    class Meta:
        model = MealSubscription
        fields = ('id', 'customer', 'plan', 'plan_name', 'start_date', 'end_date', 'selected_meals_json')
        read_only_fields = ('id', 'customer')
