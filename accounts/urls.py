from django.urls import path
from .views import SignUpView, homepage
urlpatterns = [
    path('', homepage, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('<str:ref_code>/', homepage, name='home'),
]