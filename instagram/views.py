from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Project,Votes
from .forms import ProfileForm,ProjectForm,VotesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# Create your views here.
def welcome(request):
    proj=Project.objects.all()
  
    print(proj)
    return render(request, 'index.html',{'proj':proj})
@login_required(login_url='/accounts/login/')
def prof(request):
    current_user =request.user
    user = User.objects.all()
    profiles = Profile.objects.filter(user=user).first
    
    return render(request, 'all-aww/profile.html',{"profiles":profiles},{"user":user})
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user =request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
             profile = form.save(commit=False)
             profile.user = current_user
             profile.save()
        return redirect("prof")
       
    else:
            form = ProfileForm()
    return render(request, 'new_profile.html',{"form":form})
@login_required(login_url='/accounts/login/')
def project(request):
    current_user = request.user
    if request.method =='POST':
        form =  ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        
        return redirect("home")    
    else:  
            form = ProjectForm()
    return render(request,'new_awrd.html',{"form":form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_images = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message}) 
