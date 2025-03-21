
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),  # Uncomment if you want to enable the Django admin
    path('', include("myapp.urls")), 
    path('google_fit/', include('myapp.urls')),# Includes the URLs from the 'myapp' app
]
