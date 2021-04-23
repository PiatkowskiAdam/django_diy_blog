from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from blog.models import Post, Comment
from blog.forms import AddComment
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')


class AllPostsList(generic.ListView):
    model = Post
    paginate_by = 5


class AllBloggersList(generic.ListView):
    model = User
    

class BloggerDetailView(generic.DetailView):
    model = User

class PostDetailView(generic.DetailView):
    model = Post

def add_comment(request, pk):
    form = AddComment()

    if request.method == "POST":
        form = AddComment(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail', pk=pk)

    else:
        form = AddComment()


    return render(request, 'blog/add_comment.html', {'form': form})

    