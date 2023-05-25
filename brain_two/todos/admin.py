from django.contrib import admin
from todos.models import TodoList, TodoItem


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_on",
    )


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
       "task",
       "due_date",
       "is_completed",
       "list"
    )
