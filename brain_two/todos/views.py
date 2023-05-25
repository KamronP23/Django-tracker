from django.shortcuts import render
from todos.models import TodoList, TodoItem


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todos_list": todos,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo = TodoList.objects.get(id=id)
    context = {
        "todo_list": todo
    }
    return render(request, "todos/detail.html", context)


