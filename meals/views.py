from rest_framework import generics, permissions
from .models import MealPlan, MealSubscription
from .serializers import MealPlanSerializer, MealSubscriptionSerializer

class MealPlanListView(generics.ListAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.AllowAny]

class MealSubscriptionListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealSubscription.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
