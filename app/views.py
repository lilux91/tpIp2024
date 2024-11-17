# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.services.services import getAllImages
from .layers.services.services import getAllFavourites

def index_page(request):
    return render(request, 'index.html')

# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):

    images = getAllImages
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

def search(request):
    search_msg = request.POST.get('query', '').strip()

    if search_msg:
        # Llamamos al servicio para obtener todas las imágenes que coincidan con el nombre
        images = getAllImages(input=search_msg)  # Pasamos el término de búsqueda al servicio
    else:
        # Si no hay término de búsqueda, mostramos todas las imágenes
        images = getAllImages()

    # Además, obtener la lista de favoritos del usuario si está autenticado
    favourite_list = getAllFavourites(request)

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass
