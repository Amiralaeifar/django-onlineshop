from django.shortcuts import render
from .forms import UsreRegistrationForm
from django.views import View


class UserRegisterView(View):
    form_class = UsreRegistrationForm
    
    def get(self, request):
        return render(request, 'accounts/user_register.html', {
            'form': self.form_class ,
        })
    
    
    def post(self, request):
        pass
