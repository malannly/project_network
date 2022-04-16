from . import views
from django.urls import path
app_name='posts'
namespace = 'posts'
urlpatterns = [
    path('', views.index, name='main_page'),
    path('group', views.groups, name='group_list'),
    path('group/<slug:slug>', views.group, name='group')
]
#path/путь(шаблон, обработчик)
#конверторы типов: <int:name>, <str:name>, <slug:name> - ASCII