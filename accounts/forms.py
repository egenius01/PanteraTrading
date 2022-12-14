from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Investment
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            "type":"text",
            "class":"form-control",
            "placeholder":"First Name"
        })
        self.fields['last_name'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Last Name"
        })
        self.fields['email'].widget.attrs.update({
            "type": "email",
            "class": "form-control",
            "placeholder": "E-mail"
        })

        self.fields['username'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields['address'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Address"
        })
        self.fields['password1'].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "placeholder": "Password"
        })
        self.fields['password2'].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "placeholder": "Confirm Password"
        })

    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","username","email", "address"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields = ['username', 'email']


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
