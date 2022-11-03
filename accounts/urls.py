from django.urls import path
from .views import SignUpView, homepage, FAQView
urlpatterns = [
    path('', homepage, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('FAQ', FAQView.as_view(), name='faq'),
    path('<str:ref_code>/', homepage, name='home'),
]