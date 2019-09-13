from django.urls import path
from . import views
from .views import EventsList

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/list', EventsList.as_view(), name='events_list')
]