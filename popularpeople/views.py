import os

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from popularpeople.forms import AddPostForm, UploadFileForm
from popularpeople.models import People, Category, TagPost, UploadFiles

menu = [
    {"name": "About Us", "url": "about"},
    {"name": "Add Article", "url": "add_page"},
    {"name": "Contact Us", "url": "contact"},
    {"name": "Log In", "url": "login"}
]


def index(request):
    posts = People.published.all()
    data = {
        'title': "Main Page",
        'menu': menu,
        'posts': posts,
        'cats_selected': 0
    }
    return render(request, 'popularpeople/index.html', context=data)

def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 1,
            }

    return render(request, 'popularpeople/post.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {"menu": menu, "title": "Add Article", 'form': form}
    return render(request, 'popularpeople/addpage.html', data)

def contact(request):
    return HttpResponse("Contact Us")

def login(request):
    return HttpResponse("Login")

# def handle_uploaded_file(f):
#     upload_dir = "popularpeople/uploads"
#     os.makedirs(upload_dir, exist_ok=True)
#     file_path = os.path.join(upload_dir, f.name)
#     with open(file_path, "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            UploadFiles.objects.create(file=uploaded_file)
            message = "File uploaded successfully!"
        else:
            message = "There was an error with the file upload."
    else:
        form = UploadFileForm()

    data = {'menu': menu, 'title': 'About Us', 'form': form}
    return render(request, 'popularpeople/about.html', data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = People.published.filter(cat_id=category.pk)

    data = {
        'title': f'Category: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'popularpeople/index.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=People.Status.PUBLISHED)

    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'popularpeople/index.html', context=data)

