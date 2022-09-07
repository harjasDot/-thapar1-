from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('enter',views.enter,name='enter'),
    path('exit',views.exit,name='exit'),
    path('makehuman',views.makehuman,name='makehuman'),
    path('del_task/<task_id>',views.deltask,name='del-task'),
]
