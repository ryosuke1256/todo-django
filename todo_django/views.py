from django.shortcuts import (
    render,
    redirect,
)
from django.views.generic import View, ListView, UpdateView, DeleteView
from .models import (
    Todo,
)
from django.urls import reverse_lazy
import logging


class IndexView(View):
    # ListViewでもいい
    def get(
        self,
        request,
    ):
        todos = Todo.objects.all().order_by("-updated_at")
        return render(
            request,
            "index.html",
            {"todos": todos},
        )

    # CreateViewでもいい
    def post(
        self,
        request,
    ):
        logging.info(request.POST["memo"])
        dir(request.POST["memo"])
        memo = request.POST["memo"]
        todo = Todo(memo=memo)
        todo.save()
        return redirect("/")


class UpdateTodo(UpdateView):
    template_name = "update.html"
    model = Todo
    fields = ("memo", "is_done")
    success_url = reverse_lazy("index")


class DeleteTodo(DeleteView):
    template_name = "delete.html"
    model = Todo
    success_url = reverse_lazy("index")  # urls.pyのname="index"
