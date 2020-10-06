from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from app.models import Animal
from django.views.generic import DetailView, ListView

# Create your views here.

class AnimalDetailView(DetailView):
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CatListView(ListView):
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals_list'] = Animal.objects.filter(kind='C')
        return context

class DogListView(ListView):
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals_list'] = Animal.objects.filter(kind='D')
        return context

class ParrotListView(ListView):
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals_list'] = Animal.objects.filter(kind='P')
        return context

class AnimalListView(ListView):
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def index(request):
    template = loader.get_template('index.html')
    dog = Animal.objects.filter(kind = 'D').first
    cat = Animal.objects.filter(kind = 'C').first
    parrot = Animal.objects.filter(kind = 'P').first
    animals = [cat,dog,parrot]
    data = {
        'title': 'ХэппиПэт',
        'animals': animals,
    }
    return HttpResponse(template.render(data))

def about_us(request):
    template = loader.get_template('app/about_us.html')
    return HttpResponse(template.render())

