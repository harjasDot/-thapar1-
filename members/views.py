from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
#imports for user creation form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#impoting models
from members.models import Article
# Create your views here.
def index(request):
    return render(request,'index.html')


def activities(request):
    return render(request,'activities.html')


def bookbank(request):
    return render(request,'bookbank.html')

def videos(request):
    if(request.method=='POST'):
        thumb=request.FILES['image']
        title=request.POST['title']
        link=request.POST['link']
        ins=Article(thumb=thumb,title=title,link=link)
        ins.save()
        messages.error(request, 'Notice Added successfully')
        return redirect('articles')
    allArticles=Article.objects.all()
    context={'articles':allArticles}
    return render(request,'videos.html',context)

def articles(request):
    allArticles=Article.objects.all()
    context={'articles':allArticles}
    return render(request,'articles.html',context)

def post(request):
    if(request.method=='POST'):
        thumb=request.FILES['image']
        title=request.POST['title']
        link=request.POST['link']
        ins=Article(thumb=thumb,title=title,link=link)
        ins.save()
        messages.error(request, 'Notice Added successfully')
        return redirect('articles')
    allArticles=Article.objects.all()
    context={'articles':allArticles}
    return render(request,'post.html',context)


def enter(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'WRONG DATA')
            return redirect("enter")

    return render(request,"login.html")

def exit(request):
    logout(request)
    messages.error(request, 'LOGGED OUT')
    return redirect("/")


def makehuman(request):
    if(request.method=='POST'):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # login(request, user)
            messages.error(request, 'User created')
            return redirect("enter")
        else:
            messages.error(request, 'Please fill form carefully')
            return redirect("makehuman")

        
    else:
        form=UserCreationForm()
        return render(request,"signup.html",{'form':form,})

def deltask(request,task_id): 
    task = Article.objects.get(pk=task_id)
    task.delete()
    messages.error(request, 'Task Deleted')
    return redirect('/')

