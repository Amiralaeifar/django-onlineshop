from django.shortcuts import render, redirect
from .forms import UsreRegistrationForm, UserVerifyCodeForm
from django.views import View
import random 
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):
    form_class = UsreRegistrationForm
    template_name = 'accounts/user_register.html'
    
    def get(self, request):
        return render(request, self.template_name, {
            'form': self.form_class ,
        })
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            OtpCode.objects.filter(phone_number=cd['phone_number']).delete()
            random_code = random.randint(100000, 999999)
            send_otp_code(cd['phone_number'], random_code)
            OtpCode.objects.create(phone_number=cd['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'full_name': cd['full_name'],
                'email': cd['email'],
                'phone_number': cd['phone_number'],
                'password1': cd['password1'],
            }
            messages.success(request,'we sent you a code', 'success')
            return redirect('accounts:verify_code')
        return render(request, self.template_name, {
            'form': form
        })
    
    
class UserRegisterVerifyCodeView(View):
    form_class = UserVerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify_code.html', {
            'form': form
        })
    
    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(full_name=user_session['full_name'], email=user_session['email'],
                                         phone_number=user_session['phone_number'], password=user_session['password1'])
                code_instance.delete()
                return redirect('home:home')
            messages.error(request, 'please enter the code , patiently', 'danger')
            return redirect('accounts:verify_code')
        return redirect('accounts:user_register')
    
    
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {
            'form': form,
        })
        
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in', 'success')
                return redirect('home:home')
            messages.error(request, 'unvalid information', 'danger')
            return redirect('accounts:user_login')
        return render(request, self.template_name, {
            'form': form,
        })
        

class UserLogoutView(View, LoginRequiredMixin):
    
    def get(self, request):
        logout(request)
        messages.success(request, 'logged out', 'success')
        return redirect('home:home')