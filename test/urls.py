from . import views
from django.urls import path

# import the view


urlpatterns = [
   path('', views.test_page_view, name='test-urls'),
]