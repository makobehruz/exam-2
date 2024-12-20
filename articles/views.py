from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles


def home(request):
    articles = Articles.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)

def article_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')
        if title and category and short_content and long_content and author:
            Articles.objects.create(
                title = title,
                category = category,
                short_content = short_content,
                long_content = long_content,
                author = author,
            )
            return redirect('home')
    return render(request,'articles/add-post.html')

def articles_detail(request, pk):
    articles = get_object_or_404(Articles, pk=pk)
    ctx = {'articles': articles}
    return render(request, 'articles/detail.html', ctx)

def article_category(request, category):
    articles = Articles.objects.filter(category=category)
    ctx = {
        'articles': articles,
        'category': category,
    }
    return render(request, 'articles/articles-by-category.html', ctx)