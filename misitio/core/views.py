from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy



#Se importan la librerias a utilizar


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        df_rsso = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(df_rsso.name, df_rsso)
        context['url'] = fs.url(name)

    return render(request, 'upload.html', context)
