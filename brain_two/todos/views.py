from django.shortcuts import render, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm

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


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos")
    else:
        form = TodoListForm()
    context = {
        "form": form
    }
    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    todo = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=todo.id)
    else:
        form = TodoListForm(instance=todo)
        context = {
            "form": form,
        }
        return render(request, "todos/update.html", context)


def todo_list_delete(request, id):
    todo = TodoList.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("todos")
    return render(request, "todos/delete.html")
