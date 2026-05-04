from ast import arg

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import todo
from .forms import todoForm

# Create your views here.
class todoListView(ListView):
    model = todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

class todoCreateView(CreateView):
    model = todo
    form_class = todoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')


class tododeleteView(DeleteView):
    model = todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list') 


def toggle_todo(request, pk):
    item = get_object_or_404(todo, pk=pk)
    item.completed = not item.completed
    item.save()
    return redirect('todo_list')    