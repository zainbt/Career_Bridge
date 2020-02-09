from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', BaseIndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', Contact.as_view(), name='contact'),
    path('authorization/', AuthenticationView.as_view(), name= 'authenticationapi')
]

