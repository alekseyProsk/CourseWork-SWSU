from django.shortcuts import render, redirect
from .models import Appeal
from .forms import AppealForm


def index(request):
    appeals = Appeal.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'appeals': appeals})


def about(request):
    return render(request, 'main/about.html')


def creator(request):

    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    form = AppealForm()
    context = {
        'form': form
    }
    return render(request, 'main/creator.html', context)
# Create your views here.
