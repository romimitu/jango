from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blogging.form import Postform
from .models import Post
def post_list(request):
    query=Post.objects.all()
    context={
        'posts':query,
        'title':'list'
    }
    return render(request,'index.html',context)

def post_details(request, id):
    query=get_object_or_404(Post,id=id)
    context={
        "details":query
    }
    return render(request,'post_details.html',context)

def post_create(request):
    form=Postform(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully save this post...")
        return HttpResponseRedirect(instance.absolute_url())
    context={
        'form':form
    }
    return render(request,'post_form.html',context)

def post_update(request, id):
    instance=get_object_or_404(Post,id=id)
    form=Postform(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Updated this post...")
        return HttpResponseRedirect(instance.absolute_url())
    context={
        "details":instance,
        "form":form
    }
    return render(request,'post_form.html',context)

def post_delete(request,id):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    return redirect('posts:allpost')

