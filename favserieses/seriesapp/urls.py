from django.urls import path
from .import views
from .views import update

urlpatterns = [
    path('',views.home,name="home"),
    path('watched',views.watched,name='watched'),
    path('later',views.watchlater,name='watchlater'),
    path('addwatch',views.addwatch,name='addwatch'),
    path('addwatchlater',views.addwatchlater,name='addwatchlater'),
    path('update/<int:series_id>/',views.update,name='update'),
    path('update1/<int:series_id>/',views.update1,name='update1'),
    path('delete/<int:series_id>/',views.delete,name='delete'),
    path('delete1/<int:series_id>/', views.delete1, name='delete1')
]