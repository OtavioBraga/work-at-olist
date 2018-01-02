from django.db import models
import uuid


class Category(models.Model):
    '''
        This model represent a category on databse.
        Categories can be any general or comprehensive division.
        E.g: Games > XBOX > Adventure...
    '''

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    name = models.CharField(
        max_length=255,
    )

    channel = models.ForeignKey(
        'Channel',
        on_delete=models.CASCADE
    )

    parent = models.ForeignKey(
        'Category',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('created_at', )

    def __str__(self):
        return self.name


class Channel(models.Model):
    '''
        This model represent a channel on databse.
        A channel is a way of making a product available.
        E.g: Submarino marketplace, Americanas marketplace...
    '''

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    name = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'
        ordering = ('created_at', )

    def __str__(self):
        return self.name