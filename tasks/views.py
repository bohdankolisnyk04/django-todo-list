from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    paginate_by = 5
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related('tags')


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:home")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("tasks:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:home")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
