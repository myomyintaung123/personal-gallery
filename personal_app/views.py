from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Photo
import os


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def services(request):
    if not request.user.is_authenticated:
        messages.success(request, "Please Login & Register with us")
        return redirect("/auth/login/")
    return render(request, 'services.html')


def portfolio(request):
    if not request.user.is_authenticated:
        messages.success(request, "Please Login & Register with us")
        return redirect("/auth/login/")
    return render(request, 'portfolio.html')


def contact(request):
    return render(request, 'contact.html')


def main_photo(request):
    return render(request, 'main_photo.html')


def gallery(request):
    if not request.user.is_authenticated:
        messages.success(request, "Please Login & Register with us")
        return redirect("/auth/login/")

    category = request.GET.get('category')
    #print('category:', category)

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    #photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)


def view_photo(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, "Please Login & Register with us")
        return redirect("/auth/login/")

    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})


def add_photo(request):
    if not request.user.is_authenticated:
        messages.success(request, "Please Login & Register with us")
        return redirect("/auth/login/")

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        # print('data:', data)
        # print('image:', image)

        if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
                category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')
        
    context = {'categories': categories}
    return render(request, 'add.html', context)


def delete_img(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, "Please Login & Register with us")
        return redirect("/auth/login/")

    photo = Photo.objects.get(id=pk)
    if len(photo.image) > 0:
        os.remove(photo.image.path)
    photo.delete()
    messages.success(request, "Image Deleted Successfully...")
    return redirect("gallery")

            

	




