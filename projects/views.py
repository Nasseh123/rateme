from django.shortcuts import render,redirect
from .forms import profileform,webappsform,ratingsform,commentform
from .models import Profile,webapps,ratings,comment
# Create your views here.
def index(request):
    latestprojects=webapps.getlatest()
    return render(request,'index.html',{'latestprojects':latestprojects})

def site(request,webapp_id):
    currentuser=request.user
    
    projects=webapps.getspecificproject(webapp_id)
    # print(projects.id)
    rateinstance=ratings.getinstance(projects.id)
    # print(rateinstance)
    rates=ratings.getall(webapp_id)
    # print(rates)
    userratedarray=[]
    for rated in rates:
        userratedarray.append(rated.user.id)
        # print(rated.user.id)
    
    av=ratings.averageOfuser(userratedarray,webapp_id)
    print (av)

    comments=comment.get_all(webapp_id)
    if request.method== 'POST':
        form=ratingsform(request.POST,instance=rateinstance)
        commentformd=commentform(request.POST)
        if form.is_valid():
            rat=ratings.getuserrating(currentuser.id)
            if rat:
                rating=form.save(commit=False)
                rating.user_id=currentuser.id
                rating.save()
                # avs=ratings.averageOfuser(userratedarray,webapp_id)
                # average=ratings.objects.filter(webapp_id=webapp_id).update(average=avs)
                
                message='Thanks for updating your ratings!'
                
                return redirect('site' ,webapp_id=webapp_id)
            else:
                rating=form.save(commit=False)
                rating.user_id=currentuser.id
                rating.webapp_id=webapp_id
                rating.save()
                message='Thanks for your ratings!'
            return redirect('site' ,webapp_id=webapp_id)

        elif commentformd.is_valid():
            commented=commentformd.save(commit=False)
            commented.webapp_id=webapp_id
            commented.user_id=currentuser.id
            commented.save()
            
            return redirect('site' ,webapp_id=webapp_id)

    else:
        form=ratingsform()
        commentformd=commentform()
    
    return render(request,'site.html',{'projects':projects,'form':form,'commentform':commentformd,'rates':rates,'av':av,'comments':comments})

def profile(request,username):
    current_user = request.user
    user_id=current_user.id
    profile=Profile.get_profile(username)
    # print(profile)
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
    # print(profile)
    allwebapps=webapps.get_all()
    if request.method == 'POST':
        form = webappsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('profile',username=user_id)

    else:
        form = profileform()

    return render(request,'search.html',{"form": form,'allwebapps':allwebapps})