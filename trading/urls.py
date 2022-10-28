from django.urls import path
from .views import dashboard, UserInvestmentsView, \
    TrackInvestmentView,referral_view,WithdrawalRequestView, \
    market_data, forex_heat_map, crypto_market


urlpatterns = [
    path('', dashboard, name='profile'),
    path('addinvestment', UserInvestmentsView.as_view(), name='add-investment'),
    path('track-investment',TrackInvestmentView.as_view(), name='track-investment'),
    path('withdrawals', WithdrawalRequestView.as_view(), name='withdrawals'),
    path('track-referrals', referral_view, name='referrals'),
    path('market-data', market_data, name='market_data'),
    path('forex_heat_map', forex_heat_map, name='forex_heat_map'),
    path('crypto_market', crypto_market, name='crypto_market'),
]