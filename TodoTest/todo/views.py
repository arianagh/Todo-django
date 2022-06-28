from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from todo.forms import AddCategoryForm
from todo.models import Category, Todo

User = get_user_model()


def index(request):
    return render(request, "index.html", {})


class AddCategory(LoginRequiredMixin, CreateView):

    model = Category
    template_name = "add-category.html"
    form_class = AddCategoryForm
    success_url = reverse_lazy('view_profile')
    context_object_name = 'form'

    def get_form(self, form_class=None):
        form = super(AddCategory, self).get_form(form_class)
        form.fields['user'].required = False
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class CategoryView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        categories = Category.objects.filter(user=user)
        return render(request, 'view-category.html', {'categories': categories})


class EditCategory(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['title']
    template_name = "edit-category.html"
    success_url = reverse_lazy('view_profile')


class AddTodo(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "add-todo.html"
    fields = '__all__'
    success_url = reverse_lazy('view_profile')
    context_object_name = 'form'

    def get_form(self, form_class=None):
        form = super(AddTodo, self).get_form(form_class)
        form.fields['due_date'].required = False
        return form


class EditTodo(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    template_name = "edit-todo.html"
    success_url = reverse_lazy('view_profile')


class ViewTodo(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user

        works = Todo.objects.filter(category__user=user)
        categories = {}
        for work in works:
            if work.category.title not in categories:
                categories.setdefault(work.category.title, [])
            categories[work.category.title].append(work)
        print(works)
        print(categories)
        return render(request, 'view-todo.html', {'works': works, 'categories': categories})
