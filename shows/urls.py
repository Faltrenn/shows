from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('search/', views.search, name="search"),
    path('crud/', views.crud, name="crud"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('deleteShow/<int:show_id>', views.deleteShow, name="delete"),
    path('createShow/', views.createShow, name="create"),
    path('editShow/<int:show_id>', views.editShow, name="edit"),
    path('getCities/', views.getCities, name="getCities"),
]
