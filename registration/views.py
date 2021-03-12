from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from tradersPanel.models import ProfileDetails


# Create your views here.
def signUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return HttpResponseRedirect(reverse('registration:sign_in'))
        else:
            messages.error(request, 'Error')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def loginView(request):
    if request.user.is_authenticated and request.user.is_staff is True:
        return HttpResponseRedirect(reverse('adminPanel:admin_dashboard'))
    elif request.user.is_authenticated and request.user.is_staff is False:
        return HttpResponseRedirect(reverse('tradersPanel:dashboard'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_staff is not None:
                    login(request, user)
                    if user.is_staff is False and ProfileDetails.objects.filter(User_id=request.user.id).exists():
                        return HttpResponseRedirect(reverse('tradersPanel:dashboard'))
                    elif user.is_staff:
                        return HttpResponseRedirect(reverse('adminPanel:admin_dashboard'))
                    else:
                       return HttpResponseRedirect(reverse('tradersPanel:profile_settings')) 
                else:
                    messages.error(request, 'This is not working')
            else:
                messages.error(request, 'Incorrect login details')
        return render(request, 'registration/sign_in.html',)

def signoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('registration:sign_in'))
