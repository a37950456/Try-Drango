# Model View Template (MVT)
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    my_title = "Hello World..... Welcome to Try Django"
    qs = BlogPost.objects.all()[:5]
    context = {"title": my_title, "blog_list": qs}
    
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About Us"}, {"content": "Welcome to the about page."})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        contact_form = ContactForm()

    context = {"title": "Contact Us", 
               "form": contact_form}
    return render(request, "form.html", context)

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)