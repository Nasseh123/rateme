from django.shortcuts import render
from .forms import profileform
from .models import Profile
# Create your views here.
def index(request):

    return render(request,'index.html')

def site(request):
    return render(request,'site.html')

def profile(request,username):
    current_user = request.user
    profile=Profile.get_profile(username)
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = profileform()
    return render(request, 'profile.html', {"form": form})