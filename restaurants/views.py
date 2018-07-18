from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import  ListView, UpdateView, CreateView

from .forms import TodoCreateForm
from .models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    

class TodoCreateView(LoginRequiredMixin, CreateView):
    form_class = TodoCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(TodoCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TodoCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add ToDo'
        return context

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TodoCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update2.html'
    #success_url = "/restaurants/"

    def get_context_data(self, *args, **kwargs):
        context = super(TodoUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = 'Update Todo: {}'.format(name)
        return context

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)







