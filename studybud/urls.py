
from django.contrib import admin
from django.urls import path, include



# 'room/' is the route youre going to and room after
# is the function you're invoking
urlpatterns = [
    path('admin/', admin.site.urls),
    # this is saying, use all the routes that are empty string 
    # that are included in base.url file
    path('', include('base.urls'))
  
]
