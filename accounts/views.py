from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Investment
from .models import CustomUser

from .forms import CustomUserCreationForm


def homepage(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = CustomUser.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except:
        pass
    print(request.session.get_expiry_date())

    return render(request, 'index.html', {})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        profile_id = self.request.session.get('ref_profile')
        if profile_id is not None:
            recommended_by_profile = CustomUser.objects.get(id=profile_id)
            super(SignUpView, self).form_valid(form)
            print(profile_id)
            registered_user = CustomUser.objects.get(id=form.instance.id)
            registered_user.recommended_by = recommended_by_profile
            print(registered_user.recommended_by)
            registered_user.save()
        else:
            print('this')

        return super().form_valid(form)

# def signup_view(request):
#     profile_id = request.session.get('ref_profile')
#     print('profile_id is ', profile_id)
#     form = CustomUserCreationForm(request.POST or None)
#     if form.is_valid():
#         if profile_id is not None:
#             recommended_by_profile = CustomUser.objects.get(id=profile_id)
#             instance = form.save()
