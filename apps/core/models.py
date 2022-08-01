from django.contrib.auth.models import User
from django.db import models


class TrackedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="added_%(class)s_set"
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="updated_%(class)s_set"
    )

    class Meta:
        abstract = True
