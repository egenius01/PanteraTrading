from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from accounts.models import Investment, UserInvestment, CustomUser, Withdrawals
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.mixins import  LoginRequiredMixin

@login_required
def dashboard(request):
    investment = UserInvestment.objects.filter(user=request.user)
    template_name = 'dashboard.html'
    profile = CustomUser.objects.get(username=request.user.username)
    withdrawal = Withdrawals.objects.filter(approved=True)
    with_num = [a for a in withdrawal if withdrawal]
    print(f'{len(with_num)} jjhhjhb')
    current_balance = profile.current_balance
    invest_bal = [a.deposit for a in investment if a.approved]
    print(invest_bal)
    total = 0
    for ele in range(0, len(invest_bal)):
        total = total + invest_bal[ele]
    referrals = profile.get_recommended_profiles()
    balance_list = [a.initial_balance for a in referrals]
    total_ref = 0
    for new in range(0, len(balance_list)):
        total_ref = total_ref + (balance_list[new] * 0.1)
    current_balance = total + current_balance + total_ref
    context = {'ref_count': len(balance_list),
               'current_balance': current_balance,
               'total_ref': int(total_ref),
               'with_num': len(with_num)

               }
    return render(request, template_name, context)


class UserInvestmentsView(LoginRequiredMixin, CreateView):
    model = UserInvestment
    fields = ['investment', 'deposit', 'payment_mode']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Investment.objects.order_by('id')
        return super(UserInvestmentsView, self).get_context_data(**kwargs)


class WithdrawalRequestView(LoginRequiredMixin, CreateView):
    model = Withdrawals
    fields = ['investments', 'payment_mode', 'amount']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Withdrawals.objects.order_by('date_created')
        print(kwargs['object_list'])
        return super(WithdrawalRequestView, self).get_context_data(**kwargs)

@login_required
def referral_view(request):
    profile = CustomUser.objects.get(username=request.user.username)
    referrals = profile.get_recommended_profiles()
    balance_list = [a.initial_balance for a in referrals]
    total = 0
    for ele in range(0, len(balance_list)):
        total = total + (balance_list[ele] * 0.1)
    context = {
        'ref': referrals,
        'object_list': referrals,
        'total_referrals': int(total),
    }
    return render(request, 'accounts/refferals_list.html', context)


class TrackInvestmentView(LoginRequiredMixin, ListView):
    model = UserInvestment


def market_data(request):
    return render(request, 'market_explore/market_data.html')


def forex_heat_map(request):
    return render(request, 'market_explore/forex_heat_map.html')

def crypto_market(request):
    return render(request, 'market_explore/crypto_market.html')
