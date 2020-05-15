"""mqlim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo_list import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.home, name='home'),
    path('about/', todo_views.about, name='about'),
    path('contactus/', todo_views.contact, name='contact'),
    path('listings/', todo_views.listings, name='listings'),
    path('delete/<list_id>', todo_views.delete, name='delete'),
    path('strike/<list_id>', todo_views.strike, name='strike'),
    path('unstrike/<list_id>', todo_views.unstrike, name='unstrike'),
    path('edit/<list_id>', todo_views.edit, name='edit'),
]
 	
