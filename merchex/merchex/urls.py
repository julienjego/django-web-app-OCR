"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bands/", views.band_list, name="band-list"),
    path("bands/<int:id>/", views.band_detail, name="band-detail"),
    path("bands/add/", views.band_create, name="band-create"),
    path("bands/<int:id>/change/", views.band_update, name="band-update"),
    path("bands/<int:id>/delete/", views.band_delete, name="band-delete"),
    path("about-us/", views.about, name="about-us"),
    path("items/", views.item_list, name="item-list"),
    path("items/<int:id>/", views.item_detail, name="item-detail"),
    path("items/add/", views.item_create, name="item-create"),
    path("items/<int:id>/change", views.item_update, name="item-update"),
    path("items/<int:id>/delete", views.item_delete, name="item-delete"),
    path("contact-us/", views.contact, name="contact-us"),
    path("contact-success/", views.contact_success, name="email-sent"),
]
