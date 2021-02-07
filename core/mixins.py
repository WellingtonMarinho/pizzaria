from django.db import models
import uuid

class ActiveMixin(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Cliente ativo")

    class Meta:
        abstract = True


class DateLogMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        abstract = True

class BaseModel(DateLogMixin, ActiveMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.uuid)
