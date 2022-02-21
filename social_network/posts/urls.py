from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path('group', views.groups),
    path('group/<slug:slug>', views.group)
]
#path/путь(шаблон, обработчик)
#конверторы типов: <int:name>, <str:name>, <slug:name> - ASCII