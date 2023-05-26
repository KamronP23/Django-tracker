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
        form = TodoListForm(request.post)
        if form.is_valid():
            todo = form.save(False)
            todo.save()
            return redirect("todos")
        else:
            form = TodoListForm()
        context = {
            "form": form
        }
        return render(request, "todos/create.html", context)
