"""
URL configuration for project9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from productapp.views import ProductInput,ProductInsert,ProductsDisplay,ProductDeleteInput,ProductDelete,ProductUpdateInput,ProductUpdate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('productapp/',ProductInput.as_view()),
    path('productapp/insert',ProductInsert.as_view()),
    path('productapp/display',ProductsDisplay.as_view()),
    path('productapp/deleteinput',ProductDeleteInput.as_view()),
    path('productapp/delete',ProductDelete.as_view()),
    path('productapp/updateinput',ProductUpdateInput.as_view()),
    path('productapp/update',ProductUpdate.as_view()),
]
