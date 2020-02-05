from django.urls import path
from .views import *

app_name = 'university'

urlpatterns = [
    path('uprofile/', UProfileView.as_view(), name='uprofile'),
    path('', DashBoardView.as_view(), name='dashboard'),
    path('bidding/', Bidding.as_view(), name='bidding'),
    path('project/', ProjectsView.as_view(), name='projects'),
    path('pform/', ProjectFormView.as_view(), name='pform'),
    path('colabs/', ClobsView.as_view(), name='colabs'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('bid/', CreateBid.as_view(), name='bid'),
]