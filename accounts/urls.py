from django.urls import path
from .views import SignUpView, homepage, FAQView,AboutView,BlogView
urlpatterns = [
    path('', homepage, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('FAQ', FAQView.as_view(), name='faq'),
    path('about', AboutView.as_view(), name='about'),
    path('blog', BlogView.as_view(), name='blog'),
    path('<str:ref_code>/', homepage, name='home'),
]