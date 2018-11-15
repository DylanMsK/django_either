from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from account.forms import ProfileForm


# Create your views here.
def login(request):
    # 이미 로그인 한 사람
    if request.user.is_authenticated:
        return redirect('question:list')
    # 사용자가 로그인을 요청했으면?
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('question:list')
    # 로그인을 위한 폼을 요청했으면?
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('question:list')
    
def signup(request):
    if request.user.is_authenticated:
        return redirect('question:list')
    # 사용자를 등록하는 로직
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        pro_form = ProfileForm(request.POST)
        if form.is_valid() and pro_form.is_valid():
            user = form.save()
            profile = pro_form.save(commit=False)
            profile.user = user
            profile.save()
            auth_login(request, user)
            return redirect('question:list')
    # 정보를 입력하는 폼을 전달
    else:
        form = UserCreationForm()
        pro_form = ProfileForm()
    return render(request, 'account/signup.html', {'form': form,
                                                   'pro_form': pro_form})