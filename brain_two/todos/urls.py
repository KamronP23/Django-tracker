from django.urls import path
from todos.views import todos_list_list

urlpatterns = [
    path("", todos_list_list, name="todos"),

]