from django.db import models
import uuid

from utils.exceptions import NotFoundException


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    @classmethod
    def get_or_404(self, **kwargs):
        try:
            return self.objects.get(**kwargs)
        except self.DoesNotExist:
            raise NotFoundException()
