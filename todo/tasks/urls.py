from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="list"),
    path('upadate_task/<str:pk>/',views.updateTask,name='upadate_task'),
    path('delete_task/<str:pk>/',views.deleteTask,name='delete_task'),
]