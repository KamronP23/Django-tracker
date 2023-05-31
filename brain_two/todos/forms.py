from django.forms import ModelForm
from todos.models import TodoList, TodoItem


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]


class TodoItem(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "__all__"
        ]
