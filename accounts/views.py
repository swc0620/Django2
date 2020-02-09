from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect, render, resolve_url
from .forms import SignUpForm


# Create your views here.

# 회원가입 - 함수 기반 view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 회원가입과 동시에 자동 로그인 처리
            next_url = request.GET.get('next') or 'profile'
            return redirect(next_url)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })
# 회원가입 - class 기반 view
'''
class SignupView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    
    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)
        
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())
        
signup = SignupView.as_view(
    model=User,
    form_class=SignUpForm,
    success_url=settings.LOGIN_URL,
    template_name='accounts/signup.html'
)
'''

@login_required #로그인이 된 경우에만 profile을 보여줌
def profile(request):
    return render(request, 'accounts/profile.html')