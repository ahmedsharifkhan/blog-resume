from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.models import User
from blog.templatetags import extras

def blogHome(request):
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by('-timestamp')[:5]
    paginator = Paginator(post_list, 8)
    #page = request.GET.get('page')
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)

    context={
        'allPosts': allPosts,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        

    }
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    most_recent = Post.objects.order_by('-timestamp')[:5]
    comments= BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp')
    replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('-timestamp')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'most_recent': most_recent, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)



def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSlug =request.POST.get('postSlug')
        post= Post.objects.get(slug=postSlug)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
        # comment=BlogComment(comment=comment, user=user, post=post)
        # comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")



