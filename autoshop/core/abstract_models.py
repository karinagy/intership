from django.db import models


class AbstractDefaultModels(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractDelete(models.Model):
    is_published = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        self.is_published = False
        self.save(update_fields=('is_published',))

    def alldelete(self):
        super(AbstractDelete, self).delete()

    class Meta:
        abstract = True
