from django.urls import path, include
from app.views import index, AnimalDetailView, AnimalListView, CatListView, DogListView, ParrotListView, about_us
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index),
    path('<int:pk>/', AnimalDetailView.as_view(), name='app/templates/animal-detail'),
    path('animals/', AnimalListView.as_view(), name='app/templates/animals_list'),
    path('cats/', CatListView.as_view(), name='app/templates/animals_list'),
    path('dogs/', DogListView.as_view(), name='app/templates/animals_list'),
    path('parrots/', ParrotListView.as_view(), name='app/templates/animals_list'),
    path('about_us/', about_us, name='app/templates/about_us'),
    path('parrots/<int:pk>/', AnimalDetailView.as_view(), name='app/templates/animal-detail'),
    path('cats/<int:pk>/', AnimalDetailView.as_view(), name='app/templates/animal-detail'),
    path('dogs/<int:pk>/', AnimalDetailView.as_view(), name='app/templates/animal-detail'),
]