from django.shortcuts import redirect, render
from .layers.services import getAllImages, getAllFavourites
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favourite
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

def home(request):
    images = getAllImages()  # Obtener todas las imágenes de la API

    if request.user.is_authenticated:
        favourite_list = getAllFavourites(request.user)
        for image in images:
            image.is_favourite = image.id in [fav.id for fav in favourite_list]
    else:
        favourite_list = []

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})

def search(request):
    search_msg = request.GET.get('query', '').strip()  # Usar GET para la búsqueda

    if search_msg:
        images = getAllImages(input=search_msg)  # Filtrar imágenes por búsqueda
    else:
        images = getAllImages()  # Obtener todas las imágenes si no hay búsqueda

    return render(request, 'home.html', {'images': images})

@login_required
def getAllFavouritesByUser(request):
    favourite_list = getAllFavourites(request.user)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})

@login_required
def saveFavourite(request):
    character_id = request.POST.get('character_id')
    if character_id:
        Favourite.objects.create(user=request.user, character_id=character_id)
        messages.success(request, "Personaje agregado a favoritos.")
    else:
        messages.error(request, "No se pudo agregar el personaje.")
    return redirect('home')

@login_required
def deleteFavourite(request):
    character_id = request.POST.get('character_id')
    if character_id:
        Favourite.objects.filter(user=request.user, character_id=character_id).delete()
        messages.success(request, "Personaje eliminado de favoritos.")
    else:
        messages.error(request, "No se pudo eliminar el personaje.")
    return redirect('favourites')

@login_required
def exit(request):
    logout(request)  # Cerrar sesión
    return redirect('index')
