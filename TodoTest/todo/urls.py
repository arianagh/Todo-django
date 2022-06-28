from django.urls import path

from todo.views import AddCategory, CategoryView, AddTodo, ViewTodo, EditCategory, EditTodo

urlpatterns = [
    path('view-categories/', CategoryView.as_view(), name="view-category"),
    path('adding-categories/', AddCategory.as_view(), name="add-category"),
    path('view-todo/', ViewTodo.as_view(), name="view-todo"),
    path('adding-todo/', AddTodo.as_view(), name="add-todo"),
    path('edit-category/<int:pk>', EditCategory.as_view(), name="edit-category"),
    path('edit-todo/<int:pk>', EditTodo.as_view(), name="edit-todo"),
]