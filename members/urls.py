from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('activities',views.activities,name='activities'),
    path('bookbank',views.bookbank,name='bookbank'),
    path('bookbank',views.bookbank,name='bookbank'),
    path('videos',views.videos,name='videos'),
    path('articles',views.articles,name='articles'),
    path('home',views.home,name='home_change'),
    path('enter',views.enter,name='enter'),
    path('exit',views.exit,name='exit'),
    path('makehuman',views.makehuman,name='makehuman'),
    path('del_task/<task_id>',views.deltask,name='del-task'),
]
