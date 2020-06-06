from django.shortcuts import render,redirect
from .forms import profileform,webappsform
from .models import Profile,webapps
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
    return render(request, 'profile.html', {"form": form,'profile':profile})


def search_all_projects(request):

    current_user = request.user
    user_id=current_user.id
    print(profile)
    allwebapps=webapps.get_all()
    if request.method == 'POST':
        form = webappsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('profile',username=user_id)

    else:
        form = profileform()
   
    return render(request,'search.html',{"form": form,'allwebapps':allwebapps})