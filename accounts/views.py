from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUserModel
from .forms import CustomUserCreationForm
# Create your views here.


class SignUpView(generic.CreateView):
    model = CustomUserModel
    template_name = 'accounts/sign_up.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

