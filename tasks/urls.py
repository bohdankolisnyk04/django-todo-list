from django.urls import path

from tasks.views import TaskListView, TaskCreateView, toggle_task_status, TaskUpdateView, TaskDeleteView, TagListView, \
   TagCreateView, TagDeleteView, TagUpdateView

urlpatterns = [
   path("", TaskListView.as_view(), name = "home"),
   path("tasks/create/", TaskCreateView.as_view(), name="task-form"),
   path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
   path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),

   path("<int:pk>/toggle/", toggle_task_status, name="task-toggle"),
   path("tags/", TagListView.as_view(), name="tag-list"),
   path("tags/create", TagCreateView.as_view(), name="tag-create"),
   path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
   path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),

]

app_name="tasks"
