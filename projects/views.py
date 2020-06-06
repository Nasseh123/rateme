from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')

def site(request):
    return render(request,'site.html')