from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)

    class Meta:
        ordering = ["is_done", "created_datetime"]

    def __str__(self) -> str:
        if len(self.content)>30:
            return f"{self.content[:30]}..."
        else:
            return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name