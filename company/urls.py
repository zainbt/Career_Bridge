from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'users', UserApi.as_view)
app_name = 'company'

urlpatterns = [

    path('', DashBoardView.as_view(), name='dashboard'),
    # path('dashboard/<int:pk>/', CompDetailView.as_view(), name='personal'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # new routes
    path('collaboration/', Collaborations.as_view(), name='collaborations'),
    path('projects/', Projects.as_view(), name='projects'),
    path('universities/', Universities.as_view(), name='universities'),
    path('create-project/', CreateProjectView.as_view(), name='create_project'),
    path('view-bids/', ViewBids.as_view(), name='view_bids'),
    # path('user-api/', UserApi.as_view, name='userapi'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
