from django.urls import path
from .views import home, todoList, toDo_list, todoListCreate, todoListUpdate, todoListDeelete, todoListDetail


urlpatterns = [
    path('', home),
    path('todoList/', todoList), 
    path('todoListCreate/', todoListCreate),
    path('toDo_list/', toDo_list),  
    path('todoListUpdate/<int:pk>/', todoListUpdate),
    path('todoListDeelete/<int:pk>/', todoListDeelete),       
    path('todoListDetail/<int:pk>/', todoListDetail), 
]
