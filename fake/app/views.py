from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def add(request):
    forms = PostForm(request.POST or None)
    if forms.is_valid():
        instance = forms.save(commit=True)


    context = {'forms':forms}
    return render(request, 'forms.html', context)

def display(request):
    form = Post.objects.all()
    context ={'formss':form}
    return render(request, 'display_db.html', context)