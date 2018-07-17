from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView


from restaurants.models import Todo
from django.contrib.auth.models import User

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html", {})

        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Todo.objects.filter(owner__id__in=is_following_user_ids).order_by("-updated")[:5]
        return render(request, "menus/home-feed.html", {'object_list': qs})

class UsersView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html", {})
        users = User.objects.all().exclude(username=request.user.username)
        return render(request, "menus/users.html", {'object_list': users})
