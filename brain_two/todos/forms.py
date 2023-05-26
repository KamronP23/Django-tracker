from django.forms import ModelForm
from todos.models import TodoList


class TodosListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name",
            "created_on"
        ]