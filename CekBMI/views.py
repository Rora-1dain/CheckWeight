from django.shortcuts import render
from django.db.models import Q
from .models import Article, Category



def kalkulator(request):
    return render(request, 'home/kalkulator.html')

def artikel(request):
    q = request.GET.get('q')
    category = request.GET.get('category')

    articles = Article.objects.all()

    if q:
        articles = articles.filter(title__icontains=q)

    if category and category != "all":
        articles = articles.filter(category=category)

    return render(request, 'home/artikel.html', {
    'articles': articles,
    'categories': Category.objects.all(),
    'selected_category': category,
})
