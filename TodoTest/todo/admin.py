from django.contrib import admin

from todo.models import Category, Todo

admin.site.register(Category)
admin.site.register(Todo)
