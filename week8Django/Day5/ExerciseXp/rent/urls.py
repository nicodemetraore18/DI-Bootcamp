from django.urls import path #path function
from . import views # . is shorthand for the current directory
from django.conf.urls.static import static
from django.conf import settings
# one urlpattern per line
urlpatterns = [
    path("", views.rental, name="rental"),
    path('./<int:pk>/', views.rentalint, name='rentalint'),
]
