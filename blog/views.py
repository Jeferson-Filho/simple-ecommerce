from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def news(request):
    news = Post.objects.order_by('post_date')  # Mais recentes primeiro
    return render(request, 'news.html', {'news': news})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')  # Redirecionar para listagem após salvar
    else:
        form = PostForm()
    return render(request, 'createPost.html', {'form': form})