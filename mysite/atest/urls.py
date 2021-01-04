from django.urls import path
from .import views

urlpatterns = [
    path('',    views.home_page,    name='home_page'),
    path('add_student/',    views.add_student,  name='add_student'),
    path('<int:pk>',    views.AtestationRead.as_view(), name='read_student'),
    path('<int:pk>/update', views.AtestationUpdate.as_view(),   name='update_student'),
    path('<int:pk>/delete', views.AtestationDelete.as_view(),   name='delete_student'),
]
