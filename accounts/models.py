from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .utils import generate_ref_code


class CustomUser(AbstractUser):
    address = models.CharField(max_length=100)
    initial_balance = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    currency = models.CharField(max_length=2, default='$')
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="ref_by")
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_full_name()} - {self.code}'

    def get_recommended_profiles(self):
        qs = CustomUser.objects.all()
        my_recs = [p for p in qs if p.recommended_by == self]
        return my_recs

    def referral_earning(self):
        return self.initial_balance * 0.1


    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        # if self.re
        super().save(*args, **kwargs)


class Investment(models.Model):
    plan_name = models.CharField(max_length=20)
    minimum_investment = models.CharField(max_length=50)
    maximum_investment = models.CharField(max_length=50)
    profit = models.CharField(max_length=200)
    duration = models.CharField(max_length=20)
    referral = models.CharField(max_length=20)
    capital_return = models.BooleanField()
    instant_withdrawal = models.BooleanField()

    def __str__(self):
        return self.plan_name


class UserInvestment(models.Model):
    daily = 'DAILY'
    weekly = 'WEEKLY'
    bi_weekly = 'BI-WEEKLY'
    roi_choices = ((daily, 'Daily'),
                   (weekly, 'Weekly'),
                   (bi_weekly, 'Bi-Weekly'))


    roi_choices= ((daily, 'Daily'),
                   (weekly, 'Weekly'),
                   (bi_weekly, 'Bi-Weekly'))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    roi = models.CharField(max_length=20, choices=roi_choices, default=daily)
    deposit = models.IntegerField()
    payment_mode = models.CharField(max_length=20, help_text="What Payment Method Suits You?")
    message = models.CharField(max_length=100, null=True, blank=True, default="In Progress")
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.approved:
            return f"${self.deposit} Approved"
        else:
            return f"${self.deposit} Unapproved"

    def get_absolute_url(self):
        return reverse('profile')


class Withdrawals(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    investments = models.ForeignKey(UserInvestment, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=20, help_text="Describe Method of Payment")
    approved = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='on Hold')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s {self.amount} Request {self.status}'

    def get_absolute_url(self):
        return reverse('withdrawals')

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    asked = models.DateTimeField(auto_now_add=True)
