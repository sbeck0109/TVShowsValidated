from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.add_a_new_show),
    path('shows/create', views.create),
    path('shows/<int:this_show_id>', views.display_show),
    path('shows/', views.view_all_shows),
    path('shows/<int:this_show_id>/edit', views.edit),
    path('shows/<int:this_show_id>/update', views.update),
    path('shows/<int:this_show_id>/destroy', views.destroy)

]
