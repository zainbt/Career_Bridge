from django.urls import path
from .views import *

app_name = 'profile'

urlpatterns = [

    path('about/', AboutView.as_view(), name='about'),
    path('projection/', ProfilePorjectionView.as_view(), name='projection'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('faq/', FAQ.as_view(), name='faq'),
    path('faqaccount/', AccountsFAQ.as_view(), name='faq_account'),
    path('faqbidding/', BiddingFAQ.as_view(), name='faq_bidding'),
    path('faqcontact/', ContactFAQ.as_view(), name='faq_contact'),
    path('faqproject/', ProjectsFAQ.as_view(), name='faq_project'),

]