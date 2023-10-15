
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from authorization_registration.forms import RegisterForm
from authorization_registration.models import Buyer


# Create your views here.



@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    model = Buyer
    success_url = reverse_lazy('profile')
    template_name = 'authorization_registration/authorization/registration.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
