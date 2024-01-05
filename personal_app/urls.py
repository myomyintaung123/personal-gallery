from django.urls import path
from personal_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('mainphoto/', views.main_photo, name='main_photo'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.view_photo, name='photo'),
    path('add/', views.add_photo, name='add'),
    path('delete_img/<str:pk>',views.delete_img, name='delete_img'),
]