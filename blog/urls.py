from django.urls import path
from .views import *
# from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', home, name='home'),
    # path('links/', cache_page(3600)(links), name='links'),
    path('links/', links, name='links'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('api/', api, name='api'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('sent', sent, name='sent'),
]
