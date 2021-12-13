from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from marketing.models import *
from blog.models import Post
from marketing.models import MainContent
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.http.response import HttpResponse

def home(request):
    allPosts= Post.objects.all()
    featured = Post.objects.filter(featured=True)
    slider = Post.objects.filter(slider=True).order_by('-timestamp')
    latest = Post.objects.order_by('-timestamp')[0:3]
    most_recent = Post.objects.order_by('-timestamp')[:5]
    galary = Post.objects.order_by('-timestamp')[:4]
    maincontent = MainContent.objects.filter(featured=True)
    footerSocial = FooterSocial.objects.filter(featured=True)
     # slide = Carausel.objects.all()
     # slide_featured = Carausel.objects.filter(featured=True)

    if request.method=="POST":
        email=request.POST['email']
        if len(email)<3:
               messages.error(request, "Please type a valid email")

        if User.objects.filter(email = email).first():
            messages.error(request, "You Already have Subscribed try with new one")
            return redirect('home')

        else:
               signup=Signup(email=email)
               signup.save()
               messages.success(request, "You have success fully subscribe")
    context={

        'allPosts': allPosts,
        'object_list': featured,
        'latest': latest,
        'sliders': slider,
        'most_recent': most_recent,
        'galary': galary,
        'maincontent': maincontent,
        'footerSocial': footerSocial,
     }
    return render(request, "home/index.html", context)



def about(request):
    most_recent = Post.objects.order_by('-timestamp')[:5]
    about = About.objects.filter(featured=True)
    aboutSocial = AboutSocial.objects.filter(featured=True)
    aboutbulletin = Aboutbulletin.objects.filter(featured=True)

    context={
        'about': about,
        'most_recent': most_recent,
        'aboutSocial': aboutSocial,
        'aboutbulletin': aboutbulletin,
    }
    return render(request, "home/about.html", context)



def resume(request):
    resume = Resume.objects.filter(featured=True)
    
    context={
        'resume': resume,
        
    }
    return render(request, "home/resume.html", context)




def contact(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully")
    context = {
        'latest':latest,
    }
    return render(request, "home/contact.html", context)


def search(request):
    query = request.GET["query"]
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsOverview = Post.objects.filter(overview__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsOverview, allPostsAuthor)

    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query")
    params = {
        "allPosts": allPosts,
        "query": query
    }
    
    return render(request, "home/search.html", params)








def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
          
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')

        if User.objects.filter(email = email).first():
            messages.error(request, "This email is already taken")
            return redirect('home')
     

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


# def handeLogin(request):
#     if request.method=="POST":
#         # Get the post parameters
#         loginusername=request.POST['loginusername']
#         loginpassword=request.POST['loginpassword']

#         user=authenticate(username= loginusername, password= loginpassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return redirect("home")

#     return HttpResponse("404- Not found")

def handeLogin(request):
     if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

     return HttpResponse("404- Not found")
   

     return HttpResponse("login")
   



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')