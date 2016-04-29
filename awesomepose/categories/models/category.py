from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name="children", db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "카테고리"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
