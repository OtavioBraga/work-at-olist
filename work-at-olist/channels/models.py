from django.db import models
import uuid


class Category(models.Model):
    '''
        This model represent a category on databse.
        Categories can be any general or comprehensive division.
        E.g: Games > XBOX > Adventure...
    '''

    uuid = models.CharField(
        default=uuid.uuid4,
        unique=True,
        max_length=36
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
        path = [self.name]
        next_parent = self.parent

        while next_parent is not None:
            path.append(self.parent.name)
            next_parent = next_parent.parent

        path.append(self.channel.name)

        return ' > '.join(path[::-1])


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
