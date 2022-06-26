from typing import Literal
from django.shortcuts import render
from django.urls import reverse_lazy

#import built in class based view
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

#import the model Post from models.py
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(DeleteView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

