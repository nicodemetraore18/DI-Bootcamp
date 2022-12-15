from django import forms
from .models import Todo,Category

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','details','deadline_date','category']
        widgets = {
            'name': forms.Textarea(),
            'details': forms.Textarea(),
            'deadline_date':forms.SelectDateWidget(),
        }
        labels = {
            'name': ('Writer'),
        }
        help_texts = {
            'name': ('please enter a correct name'),
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image']

