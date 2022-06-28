from django import forms

from todo.models import Todo, Category


class AddCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    class Meta:
        model = Category
        fields = ['title', 'user']

    def save(self, commit=True):
        cat = self.cleaned_data['title']
        c = Category.objects.create(title=cat, user=self.request.user)
        return c


class AddTodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
