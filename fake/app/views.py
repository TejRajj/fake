from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def forms(request):
    forms = PostForm
    context = {'forms':forms}
    return render(request, 'forms.html', context)