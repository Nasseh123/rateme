from django.shortcuts import render,redirect
from .forms import profileform
from .models import Profile
# Create your views here.
def index(request):

    return render(request,'index.html')

def site(request):
    return render(request,'site.html')

def profile(request,username):
    current_user = request.user
    user_id=current_user.id
    profile=Profile.get_profile(username)
    print(profile)
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile',username=user_id)

    else:
        form = profileform()
    return render(request, 'profile.html', {"form": form})