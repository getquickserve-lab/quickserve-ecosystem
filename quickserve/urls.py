from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/marketplace/', include('marketplace.urls')),
    path('api/logistics/', include('logistics.urls')),
    path('api/events/', include('events.urls')),
    path('api/meals/', include('meals.urls')),
]
