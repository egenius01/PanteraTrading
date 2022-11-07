from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Investment, FAQ
from .models import CustomUser
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, ContactForm


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


class FAQView(ListView):
    model = FAQ
    template_name = 'faq.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


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


def contactview(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "email.html", {"form": form})


def successview(request):
    return HttpResponse("Success! Thank you for your message.")
