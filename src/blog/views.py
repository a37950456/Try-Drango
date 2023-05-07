from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost
# Create your views here.

# get imply 1 object
# filter imply many objects

# CRUD Create Retrivev Update Delete
# Get -> Retrive / List
# Post -> Create / Update / Delete

def blog_post_list_view(request):
    qs = BlogPost.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/list.html'
    conext = {'object_list': qs} # queryset -> list of objects
    return render(request, template_name, conext)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    #list out objects
    #could be search
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        # create and save to database
        #obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.title = form.cleaned_data.get('title') # add something
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form':form}
    return render(request, template_name, context)

def blog_post_detial_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "form.html"
    context = {"title" :f"Update {obj.title}", 'form': form}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST": 
        obj.delete()
        return redirect("/blog")
    context = {"object": obj, 'form':None}
    return render(request, template_name, context)