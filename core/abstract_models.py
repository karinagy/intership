from django.db import models

from core.validators import check_raiting


class AbstractDefaultModels(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Raiting(models.Model):
    value = models.IntegerField(validators=[check_raiting], default=1)


"""
class AbstractDelete(models.Model):
    is_published = models.BooleanField(default=True)

    def Delete(self, *args, **kwargs):
        self.is_published = False
        self.save(update_fields=('is_published',))

    def Alldelet(self):
        super(AbstractDelete, self).delete()

    class Meta:
        abstract = True
"""
